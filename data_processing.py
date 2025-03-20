#import statements
import os
import sys
from snakebite.client import Client
from pyspark.sql import SparkSession
from hdf5_getters import get_desired
import io
import tables
import tempfile
from typing import List
from pyspark.sql import functions as F
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType


#Config constants
HDFS_HOST = "192.168.2.31"
HDFS_PORT = 9000
HDFS_BASE = f"hdfs://{HDFS_HOST}:{HDFS_PORT}"
SPARK_CLUSTER_URL = "spark://192.168.2.31:7077"
MSD_FOLDER_PATH_IN_HDFS = "/data/MillionSongSubset"
USER_LISTENING_DATA_PATH_IN_HDFS = "/data/train_triplets.txt"
#Choose other fileds. The ones hard coded here are necessary for the interface to function
RELEVANT_FIELDS: List[str] = [
        'artist_name',
        'title',
        'song_id'
]



def create_processed_data_df(subset_proprtion=1):
    os.environ['PYSPARK_PYTHON'] = "python3"
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    spark_session :SparkSession = SparkSession.builder \
        .master(SPARK_CLUSTER_URL) \
        .appName("spark_preprocess_driver") \
        .config("spark.dynamicAllocation.enabled", True) \
        .config("spark.executor.memory", "1g") \
        .config("spark.driver.memory", "1g") \
        .config("spark.driver.maxResultSize", "1g") \
        .getOrCreate()
        
    spark_context = spark_session.sparkContext
    spark_context.setLogLevel("ERROR")

    #Get this file by:
    #1. running "mkdir snakebite", "cd snakebite", "pip install snakebite-py3 -t .", "zip -r ../snakebite.zip .", then putting its path as an argument below
    spark_context.addPyFile("./spark_dependencies/snakebite.zip")
    #the pip package tables needs to be installed for the file below to work
    spark_context.addPyFile("./hdf5_getters.py")


    #NOTE: in case of a humongous amount of files, this will make the driver run out of memory.
    #In that case, recursion has to be implemented manually. Potential scalability weakness but
    #not close to being an issue in our case
    hdfs_client = Client(HDFS_HOST, HDFS_PORT)
    folder_to_h5_files = \
        lambda folder_path: [file_metadata["path"]  for file_metadata in list(hdfs_client.ls([folder_path], recurse=True)) \
        if file_metadata["file_type"] == "f" and file_metadata["path"].split(".")[-1] == "h5"]
    h5_file_paths_list = folder_to_h5_files(MSD_FOLDER_PATH_IN_HDFS)
    if subset_proprtion != 1:
        h5_file_paths_list = h5_file_paths_list[0:round(len(h5_file_paths_list)*subset_proprtion)]
    h5_file_paths_rdd = spark_context.parallelize(h5_file_paths_list)
    
    def get_relevant_metadata_of_song_file(file_path):
        client = Client(HDFS_HOST, HDFS_PORT)
        binary_data = b''.join(list(client.cat([file_path]))[0])
        
        file_contents = io.BytesIO(binary_data)
        

        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(file_contents.getvalue())
            temp_file_path = temp_file.name
            
            file = tables.open_file(temp_file_path)
            song_metadata = get_desired(file, RELEVANT_FIELDS)

        relevant_data = {}
        
        for field in RELEVANT_FIELDS:
            relevant_data[field] = str(song_metadata[field])
        
        return relevant_data
    
    song_data_df = spark_session.read.json(h5_file_paths_rdd.map(get_relevant_metadata_of_song_file))
    for column in song_data_df.columns:
        song_data_df = song_data_df.withColumn(
            column, F.regexp_replace(F.col(column), r"^b[\"']|[\"']$", "")
        )
    
    sqlContext = SQLContext(spark_session.sparkContext)
    user_data = sqlContext.read.csv(HDFS_BASE + USER_LISTENING_DATA_PATH_IN_HDFS, sep="\t", header=False, inferSchema=True).toDF("user_id", "song_id", "play_count")
    
    merged_df = song_data_df.join(user_data, on='song_id', how='inner').cache()
    
    return merged_df, spark_context

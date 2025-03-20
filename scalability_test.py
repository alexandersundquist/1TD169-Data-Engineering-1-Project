import time
from data_processing import create_processed_data_df 
from interface import top_songs
PROPORTIONS_OF_DATASET_TO_TEST = [0.125, 0.25, 0.5, 0.75, 1]

for proportion in PROPORTIONS_OF_DATASET_TO_TEST:
    print("proportion=",proportion)
    
    start_time = time.time()
    df, spark_session = create_processed_data_df(proportion)
    print("#create df done")
    
    top_songs(df, "093cb74eb3c517c5179ae24caf0ebec51b24d2a2", 1)
    end_time = time.time()
    print("#top songe done")
    
    print("time_elapsed=",end_time-start_time)
    
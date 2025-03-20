from pyspark.sql import functions as F
def top_songs(merged_data, user, num_songs = 3):
    user_data = merged_data.filter(merged_data['user_id'] == user)
    top_user_songs = user_data.groupBy('title').agg(F.sum('play_count').alias('Total_plays')).orderBy(F.desc('Total_plays')).limit(num_songs)
    return top_user_songs

def top_artists(merged_data, user, num_artists = 3):
    user_data = merged_data.filter(merged_data['user_id'] == user)
    top_user_artists = user_data.groupBy('artist_name').agg(F.countDistinct('song_id').alias('number_of_songs')).orderBy(F.desc('number_of_songs')).limit(num_artists)
    return top_user_artists
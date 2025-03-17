#Taken from https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py
"""
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu


This code contains a set of getters functions to access the fields
from an HDF5 song file (regular file with one song or
aggregate / summary file with many songs)

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.


Copyright 2010, Thierry Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import tables


def open_h5_file_read(h5filename):
    """
    Open an existing H5 in read mode.
    Same function as in hdf5_utils, here so we avoid one import
    """
    return tables.open_file(h5filename, mode='r')


def get_num_songs(h5):
    """
    Return the number of songs contained in this h5 file, i.e. the number of rows
    for all basic informations like name, artist, ...
    """
    return h5.root.metadata.songs.nrows

def get_artist_familiarity(h5,songidx=0):
    """
    Get artist familiarity from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_familiarity[songidx]

def get_artist_hotttnesss(h5,songidx=0):
    """
    Get artist hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_hotttnesss[songidx]

def get_artist_id(h5,songidx=0):
    """
    Get artist id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_id[songidx]

def get_artist_mbid(h5,songidx=0):
    """
    Get artist musibrainz id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_mbid[songidx]

def get_artist_playmeid(h5,songidx=0):
    """
    Get artist playme id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_playmeid[songidx]

def get_artist_7digitalid(h5,songidx=0):
    """
    Get artist 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_7digitalid[songidx]

def get_artist_latitude(h5,songidx=0):
    """
    Get artist latitude from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_latitude[songidx]

def get_artist_longitude(h5,songidx=0):
    """
    Get artist longitude from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_longitude[songidx]

def get_artist_location(h5,songidx=0):
    """
    Get artist location from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_location[songidx]

def get_artist_name(h5,songidx=0):
    """
    Get artist name from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_name[songidx]

def get_release(h5,songidx=0):
    """
    Get release from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release[songidx]

def get_release_7digitalid(h5,songidx=0):
    """
    Get release 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release_7digitalid[songidx]

def get_song_id(h5,songidx=0):
    """
    Get song id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_id[songidx]

def get_song_hotttnesss(h5,songidx=0):
    """
    Get song hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_hotttnesss[songidx]

def get_title(h5,songidx=0):
    """
    Get title from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.title[songidx]

def get_track_7digitalid(h5,songidx=0):
    """
    Get track 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.track_7digitalid[songidx]

def get_similar_artists(h5,songidx=0):
    """
    Get similar artists array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.similar_artists[h5.root.metadata.songs.cols.idx_similar_artists[songidx]:]
    return h5.root.metadata.similar_artists[h5.root.metadata.songs.cols.idx_similar_artists[songidx]:
                                            h5.root.metadata.songs.cols.idx_similar_artists[songidx+1]]

def get_artist_terms(h5,songidx=0):
    """
    Get artist terms array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                            h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_artist_terms_freq(h5,songidx=0):
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms_freq[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms_freq[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                              h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_artist_terms_weight(h5,songidx=0):
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms_weight[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms_weight[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_analysis_sample_rate(h5,songidx=0):
    """
    Get analysis sample rate from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.analysis_sample_rate[songidx]

def get_audio_md5(h5,songidx=0):
    """
    Get audio MD5 from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.audio_md5[songidx]

def get_danceability(h5,songidx=0):
    """
    Get danceability from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.danceability[songidx]

def get_duration(h5,songidx=0):
    """
    Get duration from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.duration[songidx]

def get_end_of_fade_in(h5,songidx=0):
    """
    Get end of fade in from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.end_of_fade_in[songidx]

def get_energy(h5,songidx=0):
    """
    Get energy from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.energy[songidx]

def get_key(h5,songidx=0):
    """
    Get key from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.key[songidx]

def get_key_confidence(h5,songidx=0):
    """
    Get key confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.key_confidence[songidx]

def get_loudness(h5,songidx=0):
    """
    Get loudness from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.loudness[songidx]

def get_mode(h5,songidx=0):
    """
    Get mode from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.mode[songidx]

def get_mode_confidence(h5,songidx=0):
    """
    Get mode confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.mode_confidence[songidx]

def get_start_of_fade_out(h5,songidx=0):
    """
    Get start of fade out from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.start_of_fade_out[songidx]

def get_tempo(h5,songidx=0):
    """
    Get tempo from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.tempo[songidx]

def get_time_signature(h5,songidx=0):
    """
    Get signature from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.time_signature[songidx]

def get_time_signature_confidence(h5,songidx=0):
    """
    Get signature confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.time_signature_confidence[songidx]

def get_track_id(h5,songidx=0):
    """
    Get track id from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.track_id[songidx]

def get_segments_start(h5,songidx=0):
    """
    Get segments start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_start[h5.root.analysis.songs.cols.idx_segments_start[songidx]:]
    return h5.root.analysis.segments_start[h5.root.analysis.songs.cols.idx_segments_start[songidx]:
                                           h5.root.analysis.songs.cols.idx_segments_start[songidx+1]]
    
def get_segments_confidence(h5,songidx=0):
    """
    Get segments confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_confidence[h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:]
    return h5.root.analysis.segments_confidence[h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:
                                                h5.root.analysis.songs.cols.idx_segments_confidence[songidx+1]]

def get_segments_pitches(h5,songidx=0):
    """
    Get segments pitches array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:,:]
    return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:
                                             h5.root.analysis.songs.cols.idx_segments_pitches[songidx+1],:]

def get_segments_timbre(h5,songidx=0):
    """
    Get segments timbre array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:,:]
    return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:
                                            h5.root.analysis.songs.cols.idx_segments_timbre[songidx+1],:]

def get_segments_loudness_max(h5,songidx=0):
    """
    Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_max[h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:]
    return h5.root.analysis.segments_loudness_max[h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:
                                                  h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx+1]]

def get_segments_loudness_max_time(h5,songidx=0):
    """
    Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_max_time[h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:]
    return h5.root.analysis.segments_loudness_max_time[h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:
                                                       h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx+1]]

def get_segments_loudness_start(h5,songidx=0):
    """
    Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_start[h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:]
    return h5.root.analysis.segments_loudness_start[h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:
                                                    h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx+1]]

def get_sections_start(h5,songidx=0):
    """
    Get sections start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.sections_start[h5.root.analysis.songs.cols.idx_sections_start[songidx]:]
    return h5.root.analysis.sections_start[h5.root.analysis.songs.cols.idx_sections_start[songidx]:
                                           h5.root.analysis.songs.cols.idx_sections_start[songidx+1]]

def get_sections_confidence(h5,songidx=0):
    """
    Get sections confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.sections_confidence[h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:]
    return h5.root.analysis.sections_confidence[h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:
                                                h5.root.analysis.songs.cols.idx_sections_confidence[songidx+1]]

def get_beats_start(h5,songidx=0):
    """
    Get beats start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.beats_start[h5.root.analysis.songs.cols.idx_beats_start[songidx]:]
    return h5.root.analysis.beats_start[h5.root.analysis.songs.cols.idx_beats_start[songidx]:
                                        h5.root.analysis.songs.cols.idx_beats_start[songidx+1]]

def get_beats_confidence(h5,songidx=0):
    """
    Get beats confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.beats_confidence[h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:]
    return h5.root.analysis.beats_confidence[h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:
                                             h5.root.analysis.songs.cols.idx_beats_confidence[songidx+1]]

def get_bars_start(h5,songidx=0):
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.bars_start[h5.root.analysis.songs.cols.idx_bars_start[songidx]:]
    return h5.root.analysis.bars_start[h5.root.analysis.songs.cols.idx_bars_start[songidx]:
                                       h5.root.analysis.songs.cols.idx_bars_start[songidx+1]]

def get_bars_confidence(h5,songidx=0):
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.bars_confidence[h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:]
    return h5.root.analysis.bars_confidence[h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:
                                            h5.root.analysis.songs.cols.idx_bars_confidence[songidx+1]]

def get_tatums_start(h5,songidx=0):
    """
    Get tatums start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.tatums_start[h5.root.analysis.songs.cols.idx_tatums_start[songidx]:]
    return h5.root.analysis.tatums_start[h5.root.analysis.songs.cols.idx_tatums_start[songidx]:
                                         h5.root.analysis.songs.cols.idx_tatums_start[songidx+1]]

def get_tatums_confidence(h5,songidx=0):
    """
    Get tatums confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.tatums_confidence[h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:]
    return h5.root.analysis.tatums_confidence[h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:
                                              h5.root.analysis.songs.cols.idx_tatums_confidence[songidx+1]]

def get_artist_mbtags(h5,songidx=0):
    """
    Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.musicbrainz.songs.nrows == songidx + 1:
        return h5.root.musicbrainz.artist_mbtags[h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
    return h5.root.musicbrainz.artist_mbtags[h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                             h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

def get_artist_mbtags_count(h5,songidx=0):
    """
    Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.musicbrainz.songs.nrows == songidx + 1:
        return h5.root.musicbrainz.artist_mbtags_count[h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
    return h5.root.musicbrainz.artist_mbtags_count[h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                   h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

def get_year(h5,songidx=0):
    """
    Get release year from a HDF5 song file, by default the first song in it
    """
    return h5.root.musicbrainz.songs.cols.year[songidx]

#Below are functions which were not in the original file but were included here for convenience
def get_function_data_name_pairs():
    with open('hdf5_getters.py', 'r') as file:
        for line in file:
            l = line.split(" ")
            if l[0] != "def":
                continue
            
            function_name = l[1].split("_")
            if function_name[0] != "get":
                continue
            
            
            data_name = line.split("(")[0].split(" ")[1][4:]
            print(f"(h5g.get_{data_name}, '{data_name}'),")

#Output taken from get_function_data_name_pairs and pasted in here
FUNCTION_DATA_PAIRS = [
    (get_num_songs, 'num_songs'),
    (get_artist_familiarity, 'artist_familiarity'),
    (get_artist_hotttnesss, 'artist_hotttnesss'),
    (get_artist_id, 'artist_id'),
    (get_artist_mbid, 'artist_mbid'),
    (get_artist_playmeid, 'artist_playmeid'),
    (get_artist_7digitalid, 'artist_7digitalid'),
    (get_artist_latitude, 'artist_latitude'),
    (get_artist_longitude, 'artist_longitude'),
    (get_artist_location, 'artist_location'),
    (get_artist_name, 'artist_name'),
    (get_release, 'release'),
    (get_release_7digitalid, 'release_7digitalid'),
    (get_song_id, 'song_id'),
    (get_song_hotttnesss, 'song_hotttnesss'),
    (get_title, 'title'),
    (get_track_7digitalid, 'track_7digitalid'),
    (get_similar_artists, 'similar_artists'),
    (get_artist_terms, 'artist_terms'),
    (get_artist_terms_freq, 'artist_terms_freq'),
    (get_artist_terms_weight, 'artist_terms_weight'),
    (get_analysis_sample_rate, 'analysis_sample_rate'),
    (get_audio_md5, 'audio_md5'),
    (get_danceability, 'danceability'),
    (get_duration, 'duration'),
    (get_end_of_fade_in, 'end_of_fade_in'),
    (get_energy, 'energy'),
    (get_key, 'key'),
    (get_key_confidence, 'key_confidence'),
    (get_loudness, 'loudness'),
    (get_mode, 'mode'),
    (get_mode_confidence, 'mode_confidence'),
    (get_start_of_fade_out, 'start_of_fade_out'),
    (get_tempo, 'tempo'),
    (get_time_signature, 'time_signature'),
    (get_time_signature_confidence, 'time_signature_confidence'),
    (get_track_id, 'track_id'),
    (get_segments_start, 'segments_start'),
    (get_segments_confidence, 'segments_confidence'),
    (get_segments_pitches, 'segments_pitches'),
    (get_segments_timbre, 'segments_timbre'),
    (get_segments_loudness_max, 'segments_loudness_max'),
    (get_segments_loudness_max_time, 'segments_loudness_max_time'),
    (get_segments_loudness_start, 'segments_loudness_start'),
    (get_sections_start, 'sections_start'),
    (get_sections_confidence, 'sections_confidence'),
    (get_beats_start, 'beats_start'),
    (get_beats_confidence, 'beats_confidence'),
    (get_bars_start, 'bars_start'),
    (get_bars_confidence, 'bars_confidence'),
    (get_tatums_start, 'tatums_start'),
    (get_tatums_confidence, 'tatums_confidence'),
    (get_artist_mbtags, 'artist_mbtags'),
    (get_artist_mbtags_count, 'artist_mbtags_count'),
    (get_year, 'year')
]

def get_everything(h5_file):
    data = {}
    for f, name in FUNCTION_DATA_PAIRS:
        data[name] = f(h5_file)
        
    return data

def get_desired(h5_file, desired):
    data = {}
    for f, name in FUNCTION_DATA_PAIRS:
        if name not in desired:
            continue
        data[name] = f(h5_file)
        
    return data
#!/usr/bin/env python
# coding: utf-8

import pip
import subprocess

def pip_install(package):
    subprocess.call(['pip', 'install', package])

#environment setting
import time
import re
import os
import os.path

import json

pip_install('nltk')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk.data
nltk.downloader.download('vader_lexicon')
nltk.downloader.download('stopwords')
pip_install('profanity-check')
from profanity_check import predict, predict_prob
import argparse

pip_install('coverage')
pip_install('langdetect')
pip_install('googletrans')
from googletrans import Translator
translator = Translator()
import requests, uuid

#kss2170 05/04/19 changes:
#Output of id of songs is not integers
#Unittesting implemented
#Merged all function calls into a main() function
#JSON Outputting 1007 elements, need to find out why

#def dir_given():
#    return str(args.dir_given)

def artists_list()->list:
    artists_list_ = []
    for raw_filename in os.listdir(dir_given):
        if raw_filename.endswith('.txt'):
            try:
                artist_name = raw_filename.split("~")[1].split(".txt")[0]
                if artist_name not in artists_list_:
                    artists_list_.append(artist_name)
            except IndexError:
                pass
    return artists_list_

def raw_filenames_list()->list:
    raw_filenames_list_ = []
    for raw_filename in os.listdir(dir_given):
        if raw_filename.endswith('.txt'):
            raw_filenames_list_.append(raw_filename)
    return raw_filenames_list_

def artist_s_songs_list(str)->list:
    artist_s_songs_list_ = []
    for raw_filename in raw_filenames_list():
        if str in raw_filename:
            artist_s_songs_list_.append(raw_filename)
    return artist_s_songs_list_

def song_cleaning():
    try:
        os.mkdir(dir_given + '/Cleaned_Songs')
    except FileExistsError:  
        pass
    
    for artist in set(artists_list()):
        for song in artist_s_songs_list(artist):
            f = open(dir_given + r'/' +  song, 'rb')
            all_words = ''
            for sentence in f.readlines():
                this_sentence = sentence.decode('utf-8')
                all_words += this_sentence
            #remove identifiers like chorus, verse, etc
            all_words = re.sub(r'[\(\[],.*?[\)\]]', '', all_words)
            #remove empty lines
            all_words = os.linesep.join([s for s in all_words.splitlines() if s])
            f.close()
            f = open(os.path.join(dir_given + '/Cleaned_Songs', 'cleaned_' + song ), "wb")
            f.write(all_words.encode('utf-8'))
            f.close()
    return

def artist_s_cleaned_songs_list(str)->list:
    artist_s_cleaned_songs_list_ = []
    for cleaned_raw_filename in os.listdir(dir_given + '/Cleaned_Songs/'):
        if str in cleaned_raw_filename:
#            if cleaned_raw_filename.endswith(str + '.txt') not in artist_s_cleaned_songs_list_:
            artist_s_cleaned_songs_list_.append(cleaned_raw_filename)
    return artist_s_cleaned_songs_list_
            
def id_song_to_be_scored(song_to_be_scored):

    pattern = re.compile(r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<song_title>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        id_ = match.group('id')
        return id_
    except:
        pass
    return

def artist_song_to_be_scored(song_to_be_scored):
    pattern = re.compile(r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        artist_ = match.group('artist_name').replace('-', ' ')
        return artist_
    except:
        pass
    return

def title_song_to_be_scored(song_to_be_scored):
    pattern = re.compile(r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        song_title_ = match.group('song_title').replace('-', ' ')
        return song_title_
    except:
        pass
    return

def profanity_score_min_max():
#     https://github.com/vzhou842/profanity-check
    profanity_score_list_ = []
    for artist in set(artists_list()):
        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = "" 
            f = open(dir_given + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_+" "

            song_lyrics_for_profanity_check_ = [raw_text]
            profanity_check = predict_prob(song_lyrics_for_profanity_check_)
            profanity_score = 1-float(' '.join(map(str, profanity_check)))
            profanity_score_list_.append(profanity_score)
                
    min_profanity_score_list_ = round(min(profanity_score_list_),3)
    max_profanity_score_list_ = round(max(profanity_score_list_),3)

    return min_profanity_score_list_, max_profanity_score_list_

def profanity_score(song_to_be_scored, profanity_score_min, profanity_score_max):
#     https://github.com/vzhou842/profanity-check
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = "" 

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_+" "
    
    song_lyrics_for_profanity_check_of_song_to_be_scored = [raw_text]
    profanity_check = predict_prob(song_lyrics_for_profanity_check_of_song_to_be_scored)
    profanity_score_of_song_to_be_scored = 1-float(' '.join(map(str, profanity_check)))

    regularization_step = (profanity_score_of_song_to_be_scored - profanity_score_min)/(profanity_score_max - profanity_score_min) 
    profanity_score_of_song_to_be_scored_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(profanity_score_of_song_to_be_scored_regularized,1)

def love_score_min_max():
    #Unoptimized love minmax time of 200s
    love_minmax_time = time.time()
    love_words_list_ = [
                   'adore', 'adores', 'adorable', 'affection', 'amour', 'angel', 'bliss', 
                   'care', 'caring', 'chocolate', 'companion', 'compassion', 'concern', 
                   'darling', 'dear', 'desire', 'devotion', 'endearment', 'family', 
                   'fondness', 'forever', 'friendship', 'fun', 'God', 'happiness', 'happy', 
                   'happily', 'heart', 'hugs', 'husband', 'infatuation', 'inspiration', 
                   'intimacy', 'joy', 'kiss', 'kissed', 'kisses', 
                   'love', 'loves', 'loved', 'loving', 
                   'loyalty', 'marriage', 'passion', 'relationship', 'romance', 'sex', 
                   'sweet', 'sweetheart', 'tenderness', 'trust', 'warmth', 'wife'
                    ]
    love_score_list_ = []

    for artist in set(artists_list()):   

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            with open(dir_given + '/Cleaned_Songs/' + song , 'rb') as f:
#            f = open(dir_given + '/Cleaned_Songs/' + song , 'rb')
                counter_for_love_words = 0
                for line in f.readlines():
                    this_line_wordlist = line.decode('utf-8').split()
                    for word in this_line_wordlist:
                        words_of_lyrics.append(word)
                        
                filtered_words = [word for word in words_of_lyrics if word not in stopwords.words('english') and len(word) > 1 and word not in ['na','la']] # remove the stopwords
                for item in filtered_words:
                    if item in love_words_list_:
                        counter_for_love_words += 1
                love_score = counter_for_love_words/len(filtered_words)
                love_score_rounded = round(love_score,3)
                love_score_list_.append(love_score_rounded) 
            
    min_love_score_list_ = round(min(love_score_list_),3)
    max_love_score_list_ = round(max(love_score_list_),3)
#    print("Love MinMax Time:", time.time() - love_minmax_time)

    Love_MinMax_time_ = (time.time() - love_minmax_time)
    print(f'Love MinMax runtime is: {Love_MinMax_time_:.2f} sec')
    return min_love_score_list_, max_love_score_list_

def love_score(song_to_be_scored, love_score_min, love_score_max):
    
    love_words_list_ = [
                   'adore', 'adores', 'adorable', 'affection', 'amour', 'angel', 'bliss', 
                   'care', 'caring', 'chocolate', 'companion', 'compassion', 'concern', 
                   'darling', 'dear', 'desire', 'devotion', 'endearment', 'family', 
                   'fondness', 'forever', 'friendship', 'fun', 'God', 'happiness', 'happy', 
                   'happily', 'heart', 'hugs', 'husband', 'infatuation', 'inspiration', 
                   'intimacy', 'joy', 'kiss', 'kissed', 'kisses', 
                   'love', 'loves', 'loved', 'loving', 
                   'loyalty', 'marriage', 'passion', 'relationship', 'romance', 'sex', 
                   'sweet', 'sweetheart', 'tenderness', 'trust', 'warmth', 'wife'
                    ]
    words_of_lyrics_of_song_to_be_scored = []
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    counter_for_love_words = 0
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    filtered_words = [word for word in words_of_lyrics_of_song_to_be_scored if word not in stopwords.words('english') and len(word) > 1 and word not in ['na','la']] # remove the stopwords
    for item in filtered_words:
        if item in love_words_list_:
            counter_for_love_words += 1
#     len_counter_for_love_words = len(love_words_list_)
    love_score_of_song_to_be_scored = counter_for_love_words/len(filtered_words)
    love_score_of_song_to_be_scored_rounded = round(love_score_of_song_to_be_scored,3)
    
    regularization_step = (love_score_of_song_to_be_scored_rounded - love_score_min)/(love_score_max - love_score_min) 
    love_score_of_song_to_be_scored_rounded_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(love_score_of_song_to_be_scored_rounded_regularized,1)

# i = love_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('love score=', i)

def mood_score_min_max()->float:

    sid = SentimentIntensityAnalyzer()
    mood_score_list_ = []

    for artist in set(artists_list()):   

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = "" 
            f = open(dir_given + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()         
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_+" "
            mood_score_uncompounded = sid.polarity_scores(raw_text)
            mood_score_compounded = mood_score_uncompounded['compound']
            mood_score_compounded_rounded = round(mood_score_compounded,3)
            mood_score_list_.append(mood_score_compounded_rounded) 
            
    min_mood_score_list_ = round(min(mood_score_list_),3)
    max_mood_score_list_ = round(max(mood_score_list_),3)

    return min_mood_score_list_, max_mood_score_list_

def mood_score(song_to_be_scored, mood_score_min, mood_score_max)->float:
    
    sid = SentimentIntensityAnalyzer()
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ""

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_+" "
    mood_score_uncompounded_of_song_to_be_scored = sid.polarity_scores(raw_text)
    mood_score_compounded_of_song_to_be_scored = mood_score_uncompounded_of_song_to_be_scored['compound']
    mood_score_compounded_of_song_to_be_scored_rounded = round(mood_score_compounded_of_song_to_be_scored,3)
    
    regularization_step = (mood_score_compounded_of_song_to_be_scored_rounded - mood_score_min)/(mood_score_max - mood_score_min) 
    mood_score_compounded_of_song_to_be_scored_rounded_regularized = 1*regularization_step + 0*(1-regularization_step)
    
    return round(mood_score_compounded_of_song_to_be_scored_rounded_regularized, 1)

def length_score_min_max():

    length_score_list_ = []

    for artist in set(artists_list()):   
        for song in artist_s_cleaned_songs_list(artist):
                
            num_words = 0
    
            f = open(dir_given + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
            length_score_list_.append(num_words)
            
    min_length_score_list_ = min(length_score_list_)
    max_length_score_list_ = max(length_score_list_)
                
    return min_length_score_list_, max_length_score_list_

def length_score(song_to_be_scored, length_score_min, length_score_max):
    
    num_words_of_song_to_be_scored = 0
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()            
        num_words_of_song_to_be_scored += len(this_line_wordlist)

    length_score_of_song_to_be_scored = num_words_of_song_to_be_scored
    
    regularization_step = (length_score_of_song_to_be_scored - length_score_min)/(length_score_max - length_score_min) 
    length_score_of_song_to_be_scored_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(length_score_of_song_to_be_scored_regularized,1)

def complexity_score_min_max():

    complexity_score_list_ = []

    for artist in set(artists_list()):   
        for song in artist_s_cleaned_songs_list(artist):
                    
            num_words = 0
            words_of_lyrics = []

            f = open(dir_given + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()            
                num_words += len(this_line_wordlist)
                for word_ in this_line_wordlist:
                    words_of_lyrics.append(word_)
            
            filtered_words = [word for word in words_of_lyrics if word not in stopwords.words('english') and len(word) > 1 and word not in ['na','la']] # remove the stopwords
            unique_number_of_words = len(set(filtered_words))
            number_of_words = len(words_of_lyrics)
            complexity_score = unique_number_of_words/number_of_words
            complexity_score = round(complexity_score,3)
            complexity_score_list_.append(complexity_score)
                        
    min_complexity_score_list_ = min(set(complexity_score_list_))
    max_complexity_score_list_ = max(set(complexity_score_list_))
                                    
    return min_complexity_score_list_, max_complexity_score_list_

def complexity_score(song_to_be_scored, complexity_score_min, complexity_score_max):
    
    num_words_of_song_to_be_scored = 0
    words_of_lyrics_of_song_to_be_scored = []
    
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()            
        num_words_of_song_to_be_scored += len(this_line_wordlist)
        for word_ in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word_)
    
    filtered_words_of_song_to_be_scored = [word for word in words_of_lyrics_of_song_to_be_scored if word not in stopwords.words('english') and len(word) > 1 and word not in ['na','la']] # remove the stopwords
    unique_number_of_words_of_song_to_be_scored = len(set(filtered_words_of_song_to_be_scored))
    number_of_words_of_song_to_be_scored = len(words_of_lyrics_of_song_to_be_scored)
    complexity_score_of_song_to_be_scored = unique_number_of_words_of_song_to_be_scored/number_of_words_of_song_to_be_scored
    complexity_score_of_song_to_be_scored = round(complexity_score_of_song_to_be_scored,3)
    
    regularization_step = (complexity_score_of_song_to_be_scored - complexity_score_min)/(complexity_score_max - complexity_score_min) 
    complexity_score_of_song_to_be_scored_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(complexity_score_of_song_to_be_scored_regularized, 1)

def json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max):
    dict_for_json = {}
    for artist in set(artists_list()):
        for song in artist_s_cleaned_songs_list(artist):
            dict_for_json_song = {}
            dict_for_json_song["id"] = id_song_to_be_scored(song)
            dict_for_json_song["artist"] = artist
            dict_for_json_song["title"] = title_song_to_be_scored(song)        
            dict_for_json_song["kids_safe"] = profanity_score(song, profanity_score_min, profanity_score_max)
            dict_for_json_song["love"] = love_score(song, love_score_min, love_score_max)
            dict_for_json_song["mood"] = mood_score(song, mood_score_min, mood_score_max)
            dict_for_json_song["length"] = length_score(song, length_score_min, length_score_max)
            dict_for_json_song["complexity"] = complexity_score(song, complexity_score_min, complexity_score_max)
            key, value = 'id', str(id_song_to_be_scored(song))
            if key in dict_for_json and value == dict_for_json[key]:
                print("blah")
            else:
                dict_for_json.setdefault('characterizations:', []).append(dict_for_json_song)
    print(json.dumps(dict_for_json, indent=4))

# Checking that all the songs are given a characterization:

    print(len(dict_for_json['characterizations:']))



def main():
#    global artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max
    
    artists_list_ = artists_list()
#    print("Artist Time:", time.time() - start_time)
    artist_time_ = (time.time() - start_time)
    print(f'Artist runtime is: {artist_time_:.2f} sec')
    
    raw_filenames_list_ = raw_filenames_list()
    song_cleaning()
#    print("Cleaning Time:", time.time() - start_time)
    cleaning_time_ = (time.time() - start_time)
    print(f'Cleaning runtime is: {cleaning_time_:.2f} sec')

    
    profanity_score_min, profanity_score_max = profanity_score_min_max()
    love_score_min, love_score_max = love_score_min_max()
    mood_score_min, mood_score_max = mood_score_min_max()
    length_score_min, length_score_max = length_score_min_max()
    complexity_score_min, complexity_score_max = complexity_score_min_max()
#    print("MinMax Time:", time.time() - start_time)
    MinMax_time_ = (time.time() - start_time)/60
    print(f'MinMax runtime is: {MinMax_time_:.2f} min')
    json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max)
    

if __name__ == '__main__':
    start_time = time.time()
#    dir_given = r'C:\Users\Kyle_Shipley\Documents\Columbia_Docs\IEOR 4501\ProjectTemp\TFA_Project-Alex2\TFA_Project-Alex\Lyrics'
    #    dir_given = r'C:\Users\Kyle_Shipley\Documents\Columbia_Docs\IEOR 4501\ProjectTemp\TFA_Project-Alex2\TFA_Project-Alex\Lyrics'
    parser = argparse.ArgumentParser('Parses the given directory of lyrics')
    parser.add_argument('dir_given', help='Directory of the lyrics')
    args = parser.parse_args()
    dir_given = args.dir_given
    os.chdir(dir_given)
    main()
    runtime_ = (time.time() - start_time)/60
    print(f'Total Runtime is: {runtime_:.2f} min')

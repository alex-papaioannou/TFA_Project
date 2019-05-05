#!/usr/bin/env python
# coding: utf-8

import pip
import subprocess

def pip_install(package):
    subprocess.call(['pip', 'install', package])

#environment setting
import time
import re

# Library Import and Environment Setting needed for Logistic Regression
#import numpy as np
#import matplotlib.pyplot as plt 

#plt.rc("font", size=16)
#import seaborn as sns
#sns.set(style="white")
#sns.set(style="whitegrid", color_codes=True)

import os
import os.path

import json

pip_install('nltk')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk.data
nltk.downloader.download('vader_lexicon')
nltk.downloader.download('stopwords')

# from nltk.sentiment.vader import SentimentIntensityAnalyzer

pip_install('profanity-check')
from profanity_check import predict, predict_prob

#pip_install('pip install filelock --ignore-installed')

import argparse

pip_install('coverage')
pip_install('langdetect')
#from langdetect import detect

pip_install('googletrans')
from googletrans import Translator
translator = Translator()

# !pip install py-translator
# from py_translator import Translator

# !pip install translate

# from translate import Translator
# translator = Translator(to_lang='en')

import requests, uuid

# import goslate

# imports()

# import_time = time.time()
# print(import_time - start_time)


# In[2]:


# '222~All This Time Still Falling out of Love [Album Version]~Erasure.txt'.split(".txt")[0]

#kss2170 05/04/19 changes:
#Output of id of songs is not integers
#Unittesting implemented
#Merged all function calls into a main() function
#JSON Outputting 1007 elements, need to find out why


# In[5]:


# %%time
# cell_s_t = time.time()
    
#     parser = argparse.ArgumentParser('Parses the given directory of lyrics')
#     parser.add_argument('dir_given', help='Directory of the lyrics')
#     args = parser.parse_args()
#     dir_given = args.dir_given

#Simulated 'Given' directory, needs to be changed to input from command line kss0416
# dir_given = r'C:\Users\Kyle_Shipley\Documents\Columbia_Docs\IEOR 4501\ProjectTemp\TFA_Project-Alex2\TFA_Project-Alex\Lyrics'

#Need to change path below to start in lyrics directory kss0416
# os.chdir(dir_given)

def dir_given():
    return r'/home/kss2170/Lyrics_here/Lyrics'


def artists_list()->list:
    artists_list_ = []
    for raw_filename in os.listdir(dir_given()):
        if raw_filename.endswith('.txt'):
            try:
                artist_name = raw_filename.split("~")[1].split(".txt")[0]
                if artist_name not in artists_list_:
                    artists_list_.append(artist_name)
            except IndexError:
                pass
    return artists_list_

# artists_list_ = artists_list()

def raw_filenames_list()->list:
    raw_filenames_list_ = []
    for raw_filename in os.listdir(dir_given()):
        if raw_filename.endswith('.txt'):
            raw_filenames_list_.append(raw_filename)
    return raw_filenames_list_

# raw_filenames_list_ = raw_filenames_list()

def artist_s_songs_list(str)->list:
    artist_s_songs_list_ = []
    for raw_filename in raw_filenames_list():
        if str in raw_filename:
            artist_s_songs_list_.append(raw_filename)
    return artist_s_songs_list_

def song_cleaning():
    try:
        os.mkdir(dir_given() + '/Cleaned_Songs')
    except FileExistsError:  
        pass
    
    for artist in artists_list():
        for song in artist_s_songs_list(artist):
            f = open(dir_given() + r'/' +  song, 'rb')
            all_words = ''
            for sentence in f.readlines():
                this_sentence = sentence.decode('utf-8')
                all_words += this_sentence
            #remove identifiers like chorus, verse, etc
            all_words = re.sub(r'[\(\[],.*?[\)\]]', '', all_words)
            #remove empty lines
            all_words = os.linesep.join([s for s in all_words.splitlines() if s])
            f.close()
            f = open(os.path.join(dir_given() + '/Cleaned_Songs', 'cleaned_' + song ), "wb")
            f.write(all_words.encode('utf-8'))
            f.close()
    return

# song_cleaning()

def artist_s_cleaned_songs_list(str)->list:
    artist_s_cleaned_songs_list_ = []
    for cleaned_raw_filename in os.listdir(dir_given() + '/Cleaned_Songs/'):
        if str in cleaned_raw_filename:
#            if cleaned_raw_filename.endswith(str + '.txt') not in artist_s_cleaned_songs_list_:
            artist_s_cleaned_songs_list_.append(cleaned_raw_filename)
    return artist_s_cleaned_songs_list_

# artist_s_cleaned_songs_list("The Beatles")

# def song_translating(artists_list):
#     for artist in set(artists_list):
#         for song in artist_s_songs_list(artist):
#             #Changed below to base on single given directory
#             f = open(dir_given + r'/Cleaned_Songs/cleaned_' +  song, 'rb')
#             all_words = ''
#             cleaned_songs_directory = dir_given + "/Cleaned_Songs/"

#             for sentence in f.readlines():
#                 this_sentence = sentence.decode('utf-8')
#                 try:
#                     if translator.detect(this_sentence).lang == 'en':
#                         all_words += this_sentence
#                     else:
#                         translation = translator.translate(this_sentence)
#                         all_words += translation.text
#                 except:
#                     print('exception')
#             f = open(cleaned_songs_directory + 'cleaned_' + song, 'wb')
#             f.write(all_words.encode('utf-8'))
#             f.close()
#     return

# song_translating(artists_list())
            
def id_song_to_be_scored(song_to_be_scored):

#    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
#     cleaned_song_name = song_to_be_scored.split("cleaned_")[1].split("~")[1]
    id_song_to_be_scored = int(song_to_be_scored.split("cleaned_")[1].split("~")[0])

    return id_song_to_be_scored

# a = id_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('id:', a)

def artist_song_to_be_scored(song_to_be_scored):

#    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    artist_song_to_be_scored = song_to_be_scored.split("~")[1].split(".txt")[0]
    
    return artist_song_to_be_scored

# b = artist_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('artist:', b)

def title_song_to_be_scored(song_to_be_scored):

#    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    title_song_to_be_scored = song_to_be_scored.split("~")[2].split(".txt")[0]
    
    return title_song_to_be_scored

# c = title_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('title:', c)

def profanity_score_min_max():
#     https://github.com/vzhou842/profanity-check
    profanity_score_list_ = []
    for artist in set(artists_list()):
        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = "" 
            f = open(dir_given() + '/Cleaned_Songs/' + song , 'rb')
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
                
    min_profanity_score_list_ = round(min(profanity_score_list_),2)
    max_profanity_score_list_ = round(max(profanity_score_list_),2)

    return min_profanity_score_list_, max_profanity_score_list_

# d,e = profanity_score_min_max()

# print('profanity score: min=', d, ',', 'max=', e)

# profanity_score_min, profanity_score_max = profanity_score_min_max()

def profanity_score(song_to_be_scored, profanity_score_min, profanity_score_max):
#     https://github.com/vzhou842/profanity-check
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = "" 

    f = open(dir_given() + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
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

    return round(profanity_score_of_song_to_be_scored_regularized,4)

# f = profanity_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('profanity score=', f)

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
            with open(dir_given() + '/Cleaned_Songs/' + song , 'rb') as f:
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
                love_score_rounded = round(love_score,4)
                love_score_list_.append(love_score_rounded) 
            
    min_love_score_list_ = round(min(love_score_list_),4)
    max_love_score_list_ = round(max(love_score_list_),4)
    print("Love MinMax Time:", time.time() - love_minmax_time)

    return min_love_score_list_, max_love_score_list_

# g,h = love_score_min_max()

# print('love score: min=', g, ',', 'max=', h)

# love_score_min, love_score_max = love_score_min_max()

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
    f = open(dir_given() + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
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
    love_score_of_song_to_be_scored_rounded = round(love_score_of_song_to_be_scored,4)
    
    regularization_step = (love_score_of_song_to_be_scored_rounded - love_score_min)/(love_score_max - love_score_min) 
    love_score_of_song_to_be_scored_rounded_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(love_score_of_song_to_be_scored_rounded_regularized,4)

# i = love_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('love score=', i)

def mood_score_min_max()->float:

    sid = SentimentIntensityAnalyzer()
    mood_score_list_ = []

    for artist in set(artists_list()):   

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = "" 
            f = open(dir_given() + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()         
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_+" "
            mood_score_uncompounded = sid.polarity_scores(raw_text)
            mood_score_compounded = mood_score_uncompounded['compound']
            mood_score_compounded_rounded = round(mood_score_compounded,2)
            mood_score_list_.append(mood_score_compounded_rounded) 
            
    min_mood_score_list_ = round(min(mood_score_list_),4)
    max_mood_score_list_ = round(max(mood_score_list_),4)

    return min_mood_score_list_, max_mood_score_list_

# j,k = mood_score_min_max()

# print('mood score: min=', j, ',', 'max=', k)

# mood_score_min, mood_score_max = mood_score_min_max()

def mood_score(song_to_be_scored, mood_score_min, mood_score_max)->float:
    
    sid = SentimentIntensityAnalyzer()
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ""

    f = open(dir_given() + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_+" "
    mood_score_uncompounded_of_song_to_be_scored = sid.polarity_scores(raw_text)
    mood_score_compounded_of_song_to_be_scored = mood_score_uncompounded_of_song_to_be_scored['compound']
    mood_score_compounded_of_song_to_be_scored_rounded = round(mood_score_compounded_of_song_to_be_scored,2)
    
    regularization_step = (mood_score_compounded_of_song_to_be_scored_rounded - mood_score_min)/(mood_score_max - mood_score_min) 
    mood_score_compounded_of_song_to_be_scored_rounded_regularized = 1*regularization_step + 0*(1-regularization_step)
    
    return round(mood_score_compounded_of_song_to_be_scored_rounded_regularized, 4)

# l = mood_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('mood score=', l)

def length_score_min_max():

    length_score_list_ = []

    for artist in set(artists_list()):   
        for song in artist_s_cleaned_songs_list(artist):
                
            num_words = 0
    
            f = open(dir_given() + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
            length_score_list_.append(num_words)
            
    min_length_score_list_ = min(length_score_list_)
    max_length_score_list_ = max(length_score_list_)
                
    return min_length_score_list_, max_length_score_list_

# m,n = length_score_min_max()

# print('length score: min=', m, ',', 'max=', n)

# length_score_min, length_score_max = length_score_min_max()


def length_score(song_to_be_scored, length_score_min, length_score_max):
    
    num_words_of_song_to_be_scored = 0
    f = open(dir_given() + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()            
        num_words_of_song_to_be_scored += len(this_line_wordlist)

    length_score_of_song_to_be_scored = num_words_of_song_to_be_scored
    
    regularization_step = (length_score_of_song_to_be_scored - length_score_min)/(length_score_max - length_score_min) 
    length_score_of_song_to_be_scored_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(length_score_of_song_to_be_scored_regularized,2)

# o = length_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('length score=', o)

def complexity_score_min_max():

    complexity_score_list_ = []

    for artist in set(artists_list()):   
        for song in artist_s_cleaned_songs_list(artist):
                    
            num_words = 0
            words_of_lyrics = []

            f = open(dir_given() + '/Cleaned_Songs/' + song , 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()            
                num_words += len(this_line_wordlist)
                for word_ in this_line_wordlist:
                    words_of_lyrics.append(word_)
            
            filtered_words = [word for word in words_of_lyrics if word not in stopwords.words('english') and len(word) > 1 and word not in ['na','la']] # remove the stopwords
            unique_number_of_words = len(set(filtered_words))
            number_of_words = len(words_of_lyrics)
            complexity_score = unique_number_of_words/number_of_words
            complexity_score = round(complexity_score,2)
            complexity_score_list_.append(complexity_score)
                        
    min_complexity_score_list_ = min(set(complexity_score_list_))
    max_complexity_score_list_ = max(set(complexity_score_list_))
                                    
    return min_complexity_score_list_, max_complexity_score_list_

# p,q = complexity_score_min_max()

# print('complexity score: min=', p, ',', 'max=', q)

# complexity_score_min, complexity_score_max = complexity_score_min_max()


def complexity_score(song_to_be_scored, complexity_score_min, complexity_score_max):
    
    num_words_of_song_to_be_scored = 0
    words_of_lyrics_of_song_to_be_scored = []
    
    f = open(dir_given() + '/Cleaned_Songs/' + song_to_be_scored , 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()            
        num_words_of_song_to_be_scored += len(this_line_wordlist)
        for word_ in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word_)
    
    filtered_words_of_song_to_be_scored = [word for word in words_of_lyrics_of_song_to_be_scored if word not in stopwords.words('english') and len(word) > 1 and word not in ['na','la']] # remove the stopwords
    unique_number_of_words_of_song_to_be_scored = len(set(filtered_words_of_song_to_be_scored))
    number_of_words_of_song_to_be_scored = len(words_of_lyrics_of_song_to_be_scored)
    complexity_score_of_song_to_be_scored = unique_number_of_words_of_song_to_be_scored/number_of_words_of_song_to_be_scored
    complexity_score_of_song_to_be_scored = round(complexity_score_of_song_to_be_scored,2)
    
    regularization_step = (complexity_score_of_song_to_be_scored - complexity_score_min)/(complexity_score_max - complexity_score_min) 
    complexity_score_of_song_to_be_scored_regularized = 1*regularization_step + 0*(1-regularization_step)

    return round(complexity_score_of_song_to_be_scored_regularized, 2)

# r = complexity_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('complexity score=', r)

# cell_t = time.time()
# print(cell_t - cell_s_t)

# %%time
# cell_s_t = time.time()

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
            dict_for_json.setdefault('characterizations:', []).append(dict_for_json_song)
    print(json.dumps(dict_for_json, indent=4))

# Checking that all the songs are given a characterization:

    print(len(dict_for_json['characterizations:']))

# cell_t = time.time()
# print(cell_t - cell_s_t)


# In[15]:


def main():
#    global artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max
    
    artists_list_ = artists_list()
    print("Artist Time:", time.time() - start_time)
    
    raw_filenames_list_ = raw_filenames_list()
    song_cleaning()
    print("Ceaning Time:", time.time() - start_time)
    
    profanity_score_min, profanity_score_max = profanity_score_min_max()
    love_score_min, love_score_max = love_score_min_max()
    mood_score_min, mood_score_max = mood_score_min_max()
    length_score_min, length_score_max = length_score_min_max()
    complexity_score_min, complexity_score_max = complexity_score_min_max()
    print("MinMax Time:", time.time() - start_time)
    
    json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max)
    

if __name__ == '__main__':
    start_time = time.time()
#    dir_given = r'C:\Users\Kyle_Shipley\Documents\Columbia_Docs\IEOR 4501\ProjectTemp\TFA_Project-Alex2\TFA_Project-Alex\Lyrics'
    #    dir_given = r'C:\Users\Kyle_Shipley\Documents\Columbia_Docs\IEOR 4501\ProjectTemp\TFA_Project-Alex2\TFA_Project-Alex\Lyrics'
    os.chdir(dir_given())
    main()
    print("Runtime is:", time.time() - start_time)

# In[72]


#                     if translator.detect(this_sentence).lang == 'en':
#                         all_words += this_sentence
#                     else:
#                         translation = translator.translate(this_sentence)
#                         all_words += translation.text
#                 except:
#                     pass
 
#             f.close()
#             #Deleted Directory variable and modified below line to take given directory
#             f = open(dir_given + r'/Cleaned_Songs/cleaned_' +  song, 'wb')
#             f.write(all_words.encode('utf-8'))
#             f.close()
# %time


# In[ ]:


# %time

# def song_translating(artists):
#     for artist in set(artists):
#         for song in artist_s_songs_list(artist):
#     #Changed below to base on single given directory kss0416
#             f = open(dir_given + r'/Cleaned_Songs/cleaned_' +  song, 'rb')
#             all_words = ''
#             for sentence in f.readlines():
                
#                 this_sentence = sentence.decode('utf-8')
#                 try:
#                     if translator.detect(this_sentence).lang == 'en':
#                         all_words += this_sentence
#                     else:
#                         translation = translator.translate(this_sentence)
#                         all_words += translation.text

#     #                         from time import sleep
#     #                         translator = Translator()
#     #                         translation = translator.translate(this_sentence).text
#     #                         all_words += translation
#     #                         sleep(1)
#     #                     gs = goslate.Goslate()
#     #                     translatedText = gs.translate(this_sentence,'en')
#     #                     print(translatedText)
#     #                     all_words += this_sentence
#                 except:
#                     pass
 
#             f.close()
#             #Deleted Directory variable and modified below line to take given directory
#             f = open(os.path.join(dir_given + '/Cleaned_Songs', 'cleaned_' + song ), "wb")
#             f.write(all_words.encode('utf-8'))
#             f.close()

# song_translating(artists)


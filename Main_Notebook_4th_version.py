#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python

# environment setting

import uuid
import requests
from googletrans import Translator
from langdetect import detect
import argparse
from profanity_check import predict, predict_prob
import os
import os.path
import glob
import re

import json
import time

from collections import defaultdict
from collections import Counter

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk.data
nltk.downloader.download('vader_lexicon')
nltk.downloader.download('stopwords')

get_ipython().system(' pip install profanity-check')
# https://github.com/vzhou842/profanity-check

get_ipython().system('pip install filelock --ignore-installed')


get_ipython().system('pip install coverage --ignore-installed')

get_ipython().system('pip install langdetect')

get_ipython().system('pip install mtranslate')
from mtranslate import translate
from concurrent.futures import ProcessPoolExecutor as PoolExecutor


# In[2]:


# %%time

# parser = argparse.ArgumentParser('Parses the given directory of lyrics')
# parser.add_argument('dir_given', help='Directory of the lyrics')
# args = parser.parse_args()
# dir_given = args.dir_given

# Simulated 'Given' directory, needs to be changed to input from command line kss0416


def dir_given():
    return r'/Users/alexpapaioannou/Dropbox/Personal Things/Personal/Studies Related/NY/COLUMBIA UNIVERSITY/IEOR/MSMSE/Courses/IEOR 4501 E 001 TOOLS FOR ANALYTICS/TOOLS_2019/Project_2019/Lyrics'


dir_given = '/Users/alexpapaioannou/Dropbox/Personal Things/Personal/Studies Related/NY/COLUMBIA UNIVERSITY/IEOR/MSMSE/Courses/IEOR 4501 E 001 TOOLS FOR ANALYTICS/TOOLS_2019/Project_2019/Lyrics'
os.chdir(dir_given)


def artists_list() -> list:
    artists_list_ = []
    for raw_filename in os.listdir(dir_given):
        if raw_filename.endswith('.txt'):
            try:
                artist_name = raw_filename.split("~")[1].split("~")[0]
                if artist_name not in artists_list_:
                    artists_list_.append(artist_name)
            except IndexError:
                pass
    return artists_list_


def raw_filenames_list() -> list:
    raw_filenames_list_ = []
    for raw_filename in os.listdir(dir_given):
        if raw_filename.endswith('.txt'):
            raw_filenames_list_.append(raw_filename)
    return raw_filenames_list_


def artist_s_songs_list(str) -> list:
    artist_s_songs_list_ = []
    for raw_filename in raw_filenames_list():
        if str == raw_filename.split("~")[1].split("~")[0]:
            artist_s_songs_list_.append(raw_filename)
    return artist_s_songs_list_


def song_cleaning():
    try:
        os.mkdir(dir_given + '/Cleaned_Songs/')
    except FileExistsError:
        pass

    for artist in set(artists_list()):
        for song in artist_s_songs_list(artist):
            words_of_lyrics = []
            fin = open(dir_given + r'/' + song, 'rb')
            raw_text = ""
            for line in fin.readlines():
                # remove empty lines
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_+" "
            # remove identifiers like chorus, verse, etc
            raw_text = re.sub(r"[\(\[].*?[\)\]]", "", raw_text)
            raw_text = re.sub(r'[\W+]', ' ', raw_text)
            raw_text = re.sub(r'[\s]', ' ', raw_text)
            raw_text = re.sub(r"\b[a-zA-Z]\b", "", raw_text)
            raw_text = re.sub(' +', ' ', raw_text)
            fout = open(os.path.join(dir_given +
                                     '/Cleaned_Songs', 'cleaned_' + song), "wb")
            fout.write(raw_text.encode('utf-8'))
            fin.close()
            fout.close()
    return


song_cleaning()


def artist_s_cleaned_songs_list(str) -> list:
    artist_s_cleaned_songs_list_ = []
    for cleaned_raw_filename in os.listdir(dir_given + '/Cleaned_Songs/'):
        if str == cleaned_raw_filename.split("cleaned_")[1].split("~")[1].split("~")[0]:
            if cleaned_raw_filename not in artist_s_cleaned_songs_list(str):
                artist_s_cleaned_songs_list_.append(cleaned_raw_filename)
    return artist_s_cleaned_songs_list_


def title_song_to_be_scored(song_to_be_scored):

    pattern = re.compile(
        r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        song_title_ = match.group('song_title').replace('-', ' ')
        return song_title_
    except:
        pass
    return

# c = title_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('title:', c)
artists_list_ = artists_list()

# def song_translating(artists_list_):
#     for artist in artists_list():
#         for song in artist_s_songs_list(artist):
#             if detect(title_song_to_be_scored('cleaned_'+song)) == 'en':
#                 pass
#             else:
#                 fin = open(dir_given + r'/Cleaned_Songs/cleaned_' + song, 'rb')
#                 raw_text = ''
#                 words_of_lyrics = []
#                 len_of_words_parsed = 0
#                 lines_list_ = fin.readlines()
#                 for line in lines_list_:
#                     this_line_wordlist = line.decode('utf-8').split()
#                     for word in this_line_wordlist:
#                         if word != ' ':
#                             words_of_lyrics.append(word)
#                 for word_ in words_of_lyrics:
#                     len_of_words_parsed += 1
#                     translation = translate(word_, "en", "auto")
#                     raw_text += translation + " "
#                 print(len_of_words_parsed)
#                 print(raw_text)
#                 print('\nsong has been translated')
#                 fout = open(
#                     dir_given + r'/Cleaned_Songs/cleaned_' + song, 'wb')
#                 fout.write(raw_text.encode('utf-8'))
#                 fout.close()
#                 fin.close()
#     return

# By default, it will create one Python process for each CPU in your machine
# with concurrent.futures.ProcessPoolExecutor() as executor:

#     # distribute the 1000 URLs among 4 threads in the pool
#     # _ is the body of each page that I'm ignoring right now
#     for _ in executor.map(song_translating, artists_list_):
#         pass

def id_song_to_be_scored(song_to_be_scored):

    pattern = re.compile(
        r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<song_title>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        id_ = match.group('id')
        return id_
    except:
        pass
    return

# a = id_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('id:', a)


def artist_song_to_be_scored(song_to_be_scored):

    pattern = re.compile(
        r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        artist_ = match.group('artist_name').replace('-', ' ')
        return artist_
    except:
        pass
    return

# b = artist_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('artist:', b)


def profanity_score_min_max():
    #     https://github.com/vzhou842/profanity-check
    profanity_score_list_ = []

    for artist in set(artists_list()):
        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = ""
            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
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
            f.close()

    min_profanity_score_list_ = round(min(profanity_score_list_), 3)
    max_profanity_score_list_ = round(max(profanity_score_list_), 3)

    return min_profanity_score_list_, max_profanity_score_list_


# d, e = profanity_score_min_max()

# print('profanity score: min=', d, ',', 'max=', e)


profanity_score_min, profanity_score_max = profanity_score_min_max()


def profanity_score(song_to_be_scored):
    #     https://github.com/vzhou842/profanity-check
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ""

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_+" "

    song_lyrics_for_profanity_check_of_song_to_be_scored = [raw_text]
    profanity_check = predict_prob(
        song_lyrics_for_profanity_check_of_song_to_be_scored)
    profanity_score_of_song_to_be_scored = 1 -         float(' '.join(map(str, profanity_check)))

    regularization_step = (profanity_score_of_song_to_be_scored -
                           profanity_score_min)/(profanity_score_max - profanity_score_min)
    profanity_score_of_song_to_be_scored_regularized = 1 *         regularization_step + 0*(1-regularization_step)
    f.close()
    return round(profanity_score_of_song_to_be_scored_regularized, 1)

# f = profanity_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('profanity score=', f)


def love_score_min_max():
    love_words_list_ = [
        'adore', 'adores', 'adorable', 'affection', 'amour', 'angel', 'bliss',
        #                    'care', 'caring', 'chocolate', 'companion', 'compassion', 'concern',
        #                    'darling', 'dear', 'desire', 'devotion', 'endearment', 'family',
        #                    'fondness', 'forever', 'friendship', 'fun', 'God', 'happiness', 'happy',
        'happily', 'heart', 'hugs', 'husband', 'infatuation', 'inspiration',
                   'intimacy', 'joy', 'kiss', 'kissed', 'kisses',
                   'love', 'loves', 'loved', 'loving',
        #                    'loyalty', 'marriage', 'passion', 'relationship', 'romance', 'sex',
        #                    'sweet', 'sweetheart', 'tenderness', 'trust', 'warmth', 'wife'
    ]
    love_score_list_ = []

    for artist in set(artists_list()):

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            counter_for_love_words = 0
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)

            filtered_words = [word for word in words_of_lyrics if word not in stopwords.words(
                'english') and len(word) > 1 and word not in ['na', 'la']]  # remove the stopwords
            for item in filtered_words:
                if item in love_words_list_:
                    counter_for_love_words += 1
            len_counter_for_love_words = len(love_words_list_)
            love_score = counter_for_love_words/len_counter_for_love_words
            love_score_rounded = round(love_score, 3)
            love_score_list_.append(love_score_rounded)
            f.close()

    min_love_score_list_ = round(min(love_score_list_), 3)
    max_love_score_list_ = round(max(love_score_list_), 3)

    return min_love_score_list_, max_love_score_list_

# g,h = love_score_min_max()

# print('love score: min=', g, ',', 'max=', h)


love_score_min, love_score_max = love_score_min_max()


def love_score(song_to_be_scored):

    love_words_list_ = [
        'adore', 'adores', 'adorable', 'affection', 'amour', 'angel', 'bliss',
        #                    'care', 'caring', 'chocolate', 'companion', 'compassion', 'concern',
        #                    'darling', 'dear', 'desire', 'devotion', 'endearment', 'family',
        #                    'fondness', 'forever', 'friendship', 'fun', 'God', 'happiness', 'happy',
        'happily', 'heart', 'hugs', 'husband', 'infatuation', 'inspiration',
                   'intimacy', 'joy', 'kiss', 'kissed', 'kisses',
                   'love', 'loves', 'loved', 'loving',
        #                    'loyalty', 'marriage', 'passion', 'relationship', 'romance', 'sex',
        #                    'sweet', 'sweetheart', 'tenderness', 'trust', 'warmth', 'wife'
    ]
    words_of_lyrics_of_song_to_be_scored = []
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    counter_for_love_words = 0
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    filtered_words = [word for word in words_of_lyrics_of_song_to_be_scored if word not in stopwords.words(
        'english') and len(word) > 1 and word not in ['na', 'la']]  # remove the stopwords
    for item in filtered_words:
        if item in love_words_list_:
            counter_for_love_words += 1
    len_counter_for_love_words = len(love_words_list_)
    love_score_of_song_to_be_scored = counter_for_love_words/len_counter_for_love_words
    love_score_of_song_to_be_scored_rounded = round(
        love_score_of_song_to_be_scored, 3)

    regularization_step = (love_score_of_song_to_be_scored_rounded -
                           love_score_min)/(love_score_max - love_score_min)
    love_score_of_song_to_be_scored_rounded_regularized = 1 *         regularization_step + 0*(1-regularization_step)
    f.close()

    return round(love_score_of_song_to_be_scored_rounded_regularized, 1)

# i = love_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('love score=', i)


def mood_score_min_max() -> float:
    # https://github.com/cjhutto/vaderSentiment
    sid = SentimentIntensityAnalyzer()
    mood_score_list_ = []

    for artist in set(artists_list()):

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = ""
            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_+" "
            mood_score_uncompounded = sid.polarity_scores(raw_text)
            mood_score_compounded = mood_score_uncompounded['compound']
            mood_score_compounded_rounded = round(mood_score_compounded, 3)
            mood_score_list_.append(mood_score_compounded_rounded)
            f.close()

    min_mood_score_list_ = round(min(mood_score_list_), 3)
    max_mood_score_list_ = round(max(mood_score_list_), 3)

    return min_mood_score_list_, max_mood_score_list_

# j,k = mood_score_min_max()

# print('mood score: min=', j, ',', 'max=', k)


mood_score_min, mood_score_max = mood_score_min_max()


def mood_score(song_to_be_scored) -> float:
    # https://github.com/cjhutto/vaderSentiment
    sid = SentimentIntensityAnalyzer()
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ""

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_+" "
    mood_score_uncompounded_of_song_to_be_scored = sid.polarity_scores(
        raw_text)
    mood_score_compounded_of_song_to_be_scored = mood_score_uncompounded_of_song_to_be_scored[
        'compound']
    mood_score_compounded_of_song_to_be_scored_rounded = round(
        mood_score_compounded_of_song_to_be_scored, 3)

    regularization_step = (mood_score_compounded_of_song_to_be_scored_rounded -
                           mood_score_min)/(mood_score_max - mood_score_min)
    mood_score_compounded_of_song_to_be_scored_rounded_regularized = 1 *         regularization_step + 0*(1-regularization_step)
    f.close()

    return round(mood_score_compounded_of_song_to_be_scored_rounded_regularized, 1)

# l = mood_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('mood score=', l)


def length_score_min_max():

    length_score_list_ = []

    for artist in set(artists_list()):

        for song in artist_s_cleaned_songs_list(artist):

            num_words = 0

            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
            length_score_list_.append(num_words)
            f.close()

    min_length_score_list_ = min(length_score_list_)
    max_length_score_list_ = max(length_score_list_)

    return min_length_score_list_, max_length_score_list_

# m,n = length_score_min_max()

# print('length score: min=', m, ',', 'max=', n)


length_score_min, length_score_max = length_score_min_max()


def length_score(song_to_be_scored):

    num_words_of_song_to_be_scored = 0
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        num_words_of_song_to_be_scored += len(this_line_wordlist)

    length_score_of_song_to_be_scored = num_words_of_song_to_be_scored

    regularization_step = (length_score_of_song_to_be_scored -
                           length_score_min)/(length_score_max - length_score_min)
    length_score_of_song_to_be_scored_regularized = 1 *         regularization_step + 0*(1-regularization_step)
    f.close()

    return round(length_score_of_song_to_be_scored_regularized, 1)

# o = length_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('length score=', o)


def complexity_score_min_max():

    complexity_score_list_ = []

    for artist in set(artists_list()):

        for song in artist_s_cleaned_songs_list(artist):

            num_words = 0
            words_of_lyrics = []

            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
                for word_ in this_line_wordlist:
                    words_of_lyrics.append(word_)

            filtered_words = [word for word in words_of_lyrics if word not in stopwords.words(
                'english') and len(word) > 1 and word not in ['na', 'la']]  # remove the stopwords
            unique_number_of_words = len(set(filtered_words))
            number_of_words = len(words_of_lyrics)
            try:
                complexity_score = unique_number_of_words/number_of_words
                complexity_score = round(complexity_score, 3)
                complexity_score_list_.append(complexity_score)
            except ZeroDivisionError:
                complexity_score = 0
                complexity_score = round(complexity_score, 3)
                complexity_score_list_.append(complexity_score)
                f.close()

    min_complexity_score_list_ = min(set(complexity_score_list_))
    max_complexity_score_list_ = max(set(complexity_score_list_))

    return min_complexity_score_list_, max_complexity_score_list_

# p,q = complexity_score_min_max()

# print('complexity score: min=', p, ',', 'max=', q)


complexity_score_min, complexity_score_max = complexity_score_min_max()


def complexity_score(song_to_be_scored):

    num_words_of_song_to_be_scored = 0
    words_of_lyrics_of_song_to_be_scored = []

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        num_words_of_song_to_be_scored += len(this_line_wordlist)
        for word_ in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word_)

    filtered_words_of_song_to_be_scored = [word for word in words_of_lyrics_of_song_to_be_scored if word not in stopwords.words(
        'english') and len(word) > 1 and word not in ['na', 'la']]  # remove the stopwords
    unique_number_of_words_of_song_to_be_scored = len(
        set(filtered_words_of_song_to_be_scored))
    number_of_words_of_song_to_be_scored = len(
        words_of_lyrics_of_song_to_be_scored)
    try:
        complexity_score_of_song_to_be_scored = unique_number_of_words_of_song_to_be_scored /             number_of_words_of_song_to_be_scored
        complexity_score_of_song_to_be_scored = round(
            complexity_score_of_song_to_be_scored, 3)
    except ZeroDivisionError:
        complexity_score_of_song_to_be_scored = 0
        complexity_score_of_song_to_be_scored = round(
            complexity_score_of_song_to_be_scored, 3)
    regularization_step = (complexity_score_of_song_to_be_scored -
                           complexity_score_min)/(complexity_score_max - complexity_score_min)
    complexity_score_of_song_to_be_scored_regularized = 1 *         regularization_step + 0*(1-regularization_step)
    f.close()

    return round(complexity_score_of_song_to_be_scored_regularized, 1)

# r = complexity_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('complexity score=', r)


# In[ ]:


# %%time
# def json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max):
dict_for_json = {}
for artist in set(artists_list()):   
    for song in artist_s_cleaned_songs_list(artist):
        dict_for_json_song = {}
        dict_for_json_song["id"] = id_song_to_be_scored(song)
        dict_for_json_song["artist"] = artist_song_to_be_scored(song)
        dict_for_json_song["title"] = title_song_to_be_scored(song)        
        dict_for_json_song["kids_safe"] = profanity_score(song)
        dict_for_json_song["love"] = love_score(song)
        dict_for_json_song["mood"] = mood_score(song)
        dict_for_json_song["length"] = length_score(song)
        dict_for_json_song["complexity"] = complexity_score(song)

#         key, value = 'id', str(id_song_to_be_scored(song))
#         if key in dict_for_json and value == dict_for_json[key]:
#             print("blah")
#         else:
        dict_for_json.setdefault('characterizations:', []).append(dict_for_json_song)

print(json.dumps(dict_for_json, indent=4, ensure_ascii=False
                ))

# Checking that all the songs are given a characterization:

len(dict_for_json['characterizations:'])

#     return

# def main():
# #    global artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max
#     start_time = time.time()
#     artists_list_ = artists_list()
#     print("Artist Time:", time.time() - start_time)
    
#     raw_filenames_list_ = raw_filenames_list()
#     song_cleaning()
#     print("Ceaning Time:", time.time() - start_time)
    
#     profanity_score_min, profanity_score_max = profanity_score_min_max()
#     love_score_min, love_score_max = love_score_min_max()
#     mood_score_min, mood_score_max = mood_score_min_max()
#     length_score_min, length_score_max = length_score_min_max()
#     complexity_score_min, complexity_score_max = complexity_score_min_max()
#     print("MinMax Time:", time.time() - start_time)
    
#     json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max)
#     return
# main()


# In[ ]:


# from googletrans import Translator
# translator = Translator()

# def song_translating():
#     for artist in artists_list():
#         for song in artist_s_songs_list(artist):
#             words_of_lyrics = []
#             raw_text = ""
#             if detect(song) == 'en':
#                 pass
#             else:
#                 f = open(dir_given + '/Cleaned_Songs/cleaned_' + song, 'rb')
#                 for line in f.readlines():
#                     this_line_wordlist = line.decode('utf-8').split()
#                     for word in this_line_wordlist:
#                         if word != ' ':
#                             words_of_lyrics.append(word)
#                 for word_ in words_of_lyrics:
#                     translation = translator.translate(word_).text
#                     raw_text += translation + ' '
#                 print(raw_text)
#                 f.close()
#                 f = open(dir_given + '/Cleaned_Songs/cleaned_' + song, 'wb')
#                 f.write(raw_text.encode('utf-8'))
#                 f.close()       
#     return

# song_translating()


# In[ ]:


# from googletrans import Translator
# translator = Translator()
# translator.translate('la puta').text

# from xgoogle.translate import Translator

# translate = Translator().translate
# print(translate("Ich liebe Katzen", lang_to="en"))
# print translate("I love cats", lang_to="es").encode('utf-8')
# print translate("Amo a los gatos")


# In[ ]:


# def song_translating():
#     for artist in artists_list():
#         for song in artist_s_songs_list(artist):
#             #Changed below to base on single given directory
#             f = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'rb')
#             all_words = ''
#             cleaned_songs_directory = dir_given + "/Cleaned_Songs/"

#             for sentence in f.readlines():
#                 this_sentence = sentence.decode('utf-8')
#                 try:
#                     if translator.detect(this_sentence).lang == 'en':
#                         all_words += this_sentence
#                     else:
#                         print('translating song')
#                         translation = translator.translate(this_sentence)
#                         all_words += translation.text
#                         print('song is translated')
#                 except:
#                     print('exception')
#             f = open(cleaned_songs_directory + 'cleaned_' + song, 'wb')
#             f.write(all_words.encode('utf-8'))
#             f.close()
#     return

# song_translating()

# # 653~Svefn-G-Englar~Sigur Rós.txt


# In[ ]:


# def song_translating(song):
#     fin = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'rb')
#     raw_text = ''
#     words_of_lyrics = []
#     if detect(song) == 'en':
#         print('passing')
#     else:
#         for line in fin.readlines():
#             this_line_wordlist = line.decode('utf-8').split()
#             for word in this_line_wordlist:
#                 if word != ' ':
#                     words_of_lyrics.append(word)
#         gs = goslate.Goslate()
#         for word_ in words_of_lyrics:
#             print(word_)
#             translation = gs.translate(word_, 'en')
#             raw_text += translation
#         print(raw_text)
#         print('song is translated')
#         print(raw_text.encode('utf-8'))
#         fout = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'wb')
#         fout.write(raw_text.encode('utf-8'))
#         fout.close()        
#         fin.close()
#     return
# song_translating('951~Toquinho~Samba-Em-Prelúdio.txt')

# # print(gs.translate('653~Sigur-Rós~Svefn-G-Englar.txt', 'en'))


# In[ ]:


# from translate import Translator
# translator = Translator(to_lang='en')
# translator.translate('la puta')

# translator = Translator(to_lang='en')
# translator.translate('안녕하세요.')


#WORKS
# !pip install mtranslate
# from mtranslate import translate
# translate("Ég er kominn aftur á ný Inn í þig ÞAð er svo gott að vera hér En stoppa stutt við \
#           Ég flýt um í neðarsjávar hýði Á hóteli Beintengdur við rafmagnstöfluna Og nærist \
#           Tjú, tjú Tjú, tjú En biðin gerir mig leiðan Brot hættan sparka frá mér og kall á \
#           Ég verð að fara hjálp Tjú, tjú, tjú Tjú, tjú, tjú Tjú, tjú, tjú, tjú, tjú \
#           Ég spring út og friðurinn í loft upp Baðaður nýju ljósi Ég græt og ég græt, aftengdur \
#           ÓNýttur heili settur á brjóst og mataður af svefn Svefn-g-englum Tjú, tjú, tjú Tjú, \
#           tjú, tjú Tjú","en","auto")


# In[ ]:


# final for 1 song

# !pip install mtranslate
# from mtranslate import translate
# def song_translating(song):
#     if detect(title_song_to_be_scored('cleaned_'+song)) == 'en':
#         pass
#     else:
#         fin = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'rb')
#         raw_text = ''
#         words_of_lyrics = []
#         len_of_words_parsed = 0
#         lines_list_ = fin.readlines()
#         for line in lines_list_:
#             this_line_wordlist = line.decode('utf-8').split()
#             for word in this_line_wordlist:
#                 if word != ' ':
#                     words_of_lyrics.append(word)
#         for word_ in words_of_lyrics:
#             len_of_words_parsed += 1
#             translation = translate(word_,"en","auto")
#             raw_text += translation + " "
#         print(len_of_words_parsed)
#         print(raw_text)
#         print('\nsong has been translated')
#         fout = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'wb')
#         fout.write(raw_text.encode('utf-8'))
#         fout.close()        
#         fin.close()
#     return 

# song_translating('653~Sigur-Rós~Svefn-G-Englar.txt')

# OLD NOT WORKING
# def song_translating(artists_list):
#     cleaned_songs_directory = dir_given + "/Cleaned_Songs/"
#     for artist in artists_list:
#         for song in artist_s_songs_list(artist):
#             try:
#                 if translator.detect(this_sentence).lang == 'en':
#                     pass
#                 else:
#                     f = open(cleaned_songs_directory + 'cleaned_' + song, 'rb')
#                     all_words = ''
#                     for sentence in f.readlines():
#                         this_sentence = sentence.decode('utf-8')
#                         translation = translator.translate(this_sentence)
#                         all_words += translation.text
#                     print(song)
#                     print(all_words)
#                     f.write(all_words.encode('utf-8'))
#                     f.close()
#             except:
#                 print('exception')
#     return

# song_translating(artists_list())

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


# In[ ]:


# FINALLLLL!!!!
# def song_translating():
#     for artist in artists_list():
#         for song in artist_s_songs_list(artist):
#             if detect(title_song_to_be_scored('cleaned_'+song)) == 'en':
#                 pass
#             else:
#                 fin = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'rb')
#                 raw_text = ''
#                 words_of_lyrics = []
#                 len_of_words_parsed = 0
#                 lines_list_ = fin.readlines()
#                 for line in lines_list_:
#                     this_line_wordlist = line.decode('utf-8').split()
#                     for word in this_line_wordlist:
#                         if word != ' ':
#                             words_of_lyrics.append(word)
#                 for word_ in words_of_lyrics:
#                     len_of_words_parsed += 1
#                     translation = translate(word_,"en","auto")
#                     raw_text += translation + " "
#                 print(len_of_words_parsed)
#                 print(raw_text)
#                 print('\nsong has been translated')
#                 fout = open(dir_given+ r'/Cleaned_Songs/cleaned_' +  song, 'wb')
#                 fout.write(raw_text.encode('utf-8'))
#                 fout.close()        
#                 fin.close()
#     return 

# song_translating()


# In[ ]:


# from googletrans import Translator
# translator = Translator()

# def song_translating(song):
#     words_of_lyrics = []
#     raw_text = ""
#     if detect(song) == 'en':
#         pass
#     else:
#         f = open(dir_given + '/' + song, 'rb')
#         for line in f.readlines():
#             this_line_wordlist = line.decode('utf-8').split()
#             for word in this_line_wordlist:
#                 if word != ' ':
#                     words_of_lyrics.append(word)
#         for word_ in words_of_lyrics:
#             raw_text += word_ + ' '
#         translation = translator.translate('cabron').text
#         print(translation)
#         f.close()
#         f = open(dir_given + '/Cleaned_Songs/cleaned_' + song, 'wb')
#         f.write(raw_text.encode('utf-8'))
#         f.close()       
#     return

# song_translating('653~Sigur-Rós~Svefn-G-Englar.txt')
# translation = translator.translate('cabron').text


# In[ ]:


# pip install pipreqs
# pipreqs /Users/alexpapaioannou/Downloads/TFA_Project-Kyle


# https://pip.pypa.io/en/stable/user_guide/#requirements-files


# In[ ]:


#!/usr/bin/python
# -*- coding: utf-8 -*-

# %%time

# parser = argparse.ArgumentParser('Parses the given directory of lyrics')
# parser.add_argument('dir_given', help='Directory of the lyrics')
# args = parser.parse_args()
# dir_given = args.dir_given

# Simulated 'Given' directory, needs to be changed to input from command line kss0416

dir_given =     '/Users/alexpapaioannou/Dropbox/Personal Things/Personal/Studies Related/NY/COLUMBIA UNIVERSITY/IEOR/MSMSE/Courses/IEOR 4501 E 001 TOOLS FOR ANALYTICS/TOOLS_2019/Project_2019/Lyrics'

# Need to change path below to start in lyrics directory kss0416

os.chdir(dir_given)


def artists_list():
    artists_list_ = []
    for raw_filename in os.listdir(dir_given):
        if raw_filename.endswith('.txt'):
            try:
                artist_name = raw_filename.split('~')[2].split('.txt'
                                                               )[0]
                if artist_name not in artists_list_:
                    artists_list_.append(artist_name)
            except IndexError:
                pass
    return artists_list_


def raw_filenames_list():
    raw_filenames_list_ = []
    for raw_filename in os.listdir(dir_given):
        if raw_filename.endswith('.txt'):
            raw_filenames_list_.append(raw_filename)
    return raw_filenames_list_


def artist_s_songs_list(str):
    artist_s_songs_list_ = []
    for raw_filename in raw_filenames_list():
        if raw_filename.endswith(str + '.txt'):
            artist_s_songs_list_.append(raw_filename)
    return artist_s_songs_list_


def artist_s_cleaned_songs_list(str):
    artist_s_cleaned_songs_list_ = []
    for cleaned_raw_filename in os.listdir(dir_given + '/Cleaned_Songs/'
                                           ):
        if cleaned_raw_filename.endswith(str + '.txt') is True:
            if cleaned_raw_filename.endswith(str + '.txt')                     not in artist_s_cleaned_songs_list_:
                artist_s_cleaned_songs_list_.append(cleaned_raw_filename)
    return artist_s_cleaned_songs_list_


artist_s_cleaned_songs_list('The Beatles')


def song_cleaning():
    for artist in artists_list():
        for song in artist_s_songs_list(artist):
            f = open('Lyrics/' + song, 'rb')
            all_words = ''
            for sentence in f.readlines():
                this_sentence = sentence.decode('utf-8')
                all_words += this_sentence

            # remove identifiers like chorus, verse, etc

            all_words = re.sub(r'[\(\[],.*?[\)\]]', '', all_words)

            # remove empty lines

            all_words = os.linesep.join([s for s in
                                         all_words.splitlines() if s])
            f.close()
            directory = 'Lyrics/Cleaned_Songs'
            f = open(os.path.join(directory, 'cleaned_' + song), 'wb')
            f.write(all_words.encode('utf-8'))
            f.close()
    return


# def song_translating(artists_list):
#     cleaned_songs_directory = dir_given + "/Cleaned_Songs/"
#     for artist in artists_list:
#         for song in artist_s_songs_list(artist):
#             try:
#                 if translator.detect(this_sentence).lang == 'en':
#                     pass
#                 else:
#                     f = open(cleaned_songs_directory + 'cleaned_' + song, 'rb')
#                     all_words = ''
#                     for sentence in f.readlines():
#                         this_sentence = sentence.decode('utf-8')
#                         translation = translator.translate(this_sentence)
#                         all_words += translation.text
#                     print(song)
#                     print(all_words)
#                     f.write(all_words.encode('utf-8'))
#                     f.close()
#             except:
#                 print('exception')
#     return

# song_translating(artists_list())

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

    pattern = re.compile(r'(cleaned_)(\d+)(~)(\D+)(~)(\D+)(.txt)')
    match = pattern.match(song_to_be_scored)
    if match is True:
        try:
            id_ = match.group(2)
            return id_
        except:
            pass
    else:
        pattern = re.compile(r'(\d+)(~)(\D+)(~)(\D+)(.txt)')
        match = pattern.match(song_to_be_scored)
        try:
            id_ = match.group(1)
            return id_
        except:
            pass
    return


# a = id_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('id:', a)

def artist_song_to_be_scored(song_to_be_scored):

    pattern = re.compile(r'(cleaned_)(\d+)(~)(\D+)(~)(\D+)(.txt)')
    match = pattern.match(song_to_be_scored)
    if match is True:
        try:
            artist_ = match.group(6)
            return artist_
        except:
            pass
    else:
        pattern = re.compile(r'(\d+)(~)(\D+)(~)(\D+)(.txt)')
        match = pattern.match(song_to_be_scored)
        try:
            artist_ = match.group(5)
            return artist_
        except:
            pass
    return


# b = artist_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('artist:', b)

def title_song_to_be_scored(song_to_be_scored):

    pattern = re.compile(r'(cleaned_)(\d+)(~)(\D+)(~)(\D+)(.txt)')
    match = pattern.match(song_to_be_scored)
    if match is True:
        try:
            song_title_ = match.group(4)
            return song_title_
        except:
            pass
    else:
        pattern = re.compile(r'(\d+)(~)(\D+)(~)(\D+)(.txt)')
        match = pattern.match(song_to_be_scored)
        try:
            song_title_ = match.group(3)
            return song_title_
        except:
            pass
    return


# c = title_song_to_be_scored('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('title:', c)

def profanity_score_min_max():

    #     https://github.com/vzhou842/profanity-check

    profanity_score_list_ = []

    for artist in artists_list():

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = ''
            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            f.close()
            for word_ in words_of_lyrics:
                raw_text += word_ + ' '

            song_lyrics_for_profanity_check_ = [raw_text]
            profanity_check =                 predict_prob(song_lyrics_for_profanity_check_)
            profanity_score = 1 - float(' '.join(map(str,
                                                     profanity_check)))
            profanity_score_list_.append(profanity_score)

    min_profanity_score_list_ = round(min(profanity_score_list_), 2)
    max_profanity_score_list_ = round(max(profanity_score_list_), 2)

    return (min_profanity_score_list_, max_profanity_score_list_)


# d,e = profanity_score_min_max()

# print('profanity score: min=', d, ',', 'max=', e)

(profanity_score_min, profanity_score_max) = profanity_score_min_max()


def profanity_score(song_to_be_scored):

    #     https://github.com/vzhou842/profanity-check

    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ''

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    f.close()
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_ + ' '

    song_lyrics_for_profanity_check_of_song_to_be_scored = [raw_text]
    profanity_check =         predict_prob(song_lyrics_for_profanity_check_of_song_to_be_scored)
    profanity_score_of_song_to_be_scored = 1 - float(' '.join(map(str,
                                                                  profanity_check)))

    regularization_step = (profanity_score_of_song_to_be_scored
                           - profanity_score_min) \
        / (profanity_score_max - profanity_score_min)
    profanity_score_of_song_to_be_scored_regularized = 1         * regularization_step + 0 * (1 - regularization_step)

    return round(profanity_score_of_song_to_be_scored_regularized, 4)


# f = profanity_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('profanity score=', f)

def love_score_min_max():
    love_words_list_ = [  # 'care', 'caring', 'chocolate', 'companion', 'compassion', 'concern',
                          #                    'darling', 'dear', 'desire', 'devotion', 'endearment', 'family',
                          #                    'fondness', 'forever', 'friendship', 'fun', 'God', 'happiness', 'happy',
        'adore',
        'adores',
        'adorable',
        'affection',
        'amour',
        'angel',
        'bliss',
        'happily',
        'heart',
        'hugs',
        'husband',
        'infatuation',
        'inspiration',
        'intimacy',
        'joy',
        'kiss',
        'kissed',
        'kisses',
        'love',
        'loves',
        'loved',
        'loving',
    ]

#                    'loyalty', 'marriage', 'passion', 'relationship', 'romance', 'sex',
#                    'sweet', 'sweetheart', 'tenderness', 'trust', 'warmth', 'wife'

    love_score_list_ = []

    for artist in artists_list():

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            counter_for_love_words = 0
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            f.close()

            filtered_words = [word for word in words_of_lyrics if word
                              not in stopwords.words('english')
                              and len(word) > 1 and word not in ['na',
                                                                 'la']]  # remove the stopwords
            for item in filtered_words:
                if item in love_words_list_:
                    counter_for_love_words += 1
            len_counter_for_love_words = len(love_words_list_)
            love_score = counter_for_love_words                 / len_counter_for_love_words
            love_score_rounded = round(love_score, 4)
            love_score_list_.append(love_score_rounded)

    min_love_score_list_ = round(min(love_score_list_), 4)
    max_love_score_list_ = round(max(love_score_list_), 4)

    return (min_love_score_list_, max_love_score_list_)


# g,h = love_score_min_max()

# print('love score: min=', g, ',', 'max=', h)

(love_score_min, love_score_max) = love_score_min_max()


def love_score(song_to_be_scored):

    love_words_list_ = [  # 'care', 'caring', 'chocolate', 'companion', 'compassion', 'concern',
                          #                    'darling', 'dear', 'desire', 'devotion', 'endearment', 'family',
                          #                    'fondness', 'forever', 'friendship', 'fun', 'God', 'happiness', 'happy',
        'adore',
        'adores',
        'adorable',
        'affection',
        'amour',
        'angel',
        'bliss',
        'happily',
        'heart',
        'hugs',
        'husband',
        'infatuation',
        'inspiration',
        'intimacy',
        'joy',
        'kiss',
        'kissed',
        'kisses',
        'love',
        'loves',
        'loved',
        'loving',
    ]

#                    'loyalty', 'marriage', 'passion', 'relationship', 'romance', 'sex',
#                    'sweet', 'sweetheart', 'tenderness', 'trust', 'warmth', 'wife'

    words_of_lyrics_of_song_to_be_scored = []
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    counter_for_love_words = 0
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    filtered_words = [word for word in
                      words_of_lyrics_of_song_to_be_scored if word
                      not in stopwords.words('english') and len(word)
                      > 1 and word not in ['na', 'la']]  # remove the stopwords
    for item in filtered_words:
        if item in love_words_list_:
            counter_for_love_words += 1
    len_counter_for_love_words = len(love_words_list_)
    love_score_of_song_to_be_scored = counter_for_love_words         / len_counter_for_love_words
    love_score_of_song_to_be_scored_rounded =         round(love_score_of_song_to_be_scored, 4)

    regularization_step = (love_score_of_song_to_be_scored_rounded
                           - love_score_min) / (love_score_max
                                                - love_score_min)
    love_score_of_song_to_be_scored_rounded_regularized = 1         * regularization_step + 0 * (1 - regularization_step)

    return round(love_score_of_song_to_be_scored_rounded_regularized, 4)


# i = love_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('love score=', i)

def mood_score_min_max():

    # https://github.com/cjhutto/vaderSentiment

    sid = SentimentIntensityAnalyzer()
    mood_score_list_ = []

    for artist in artists_list():

        for song in artist_s_cleaned_songs_list(artist):
            words_of_lyrics = []
            raw_text = ''
            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_ + ' '
            mood_score_uncompounded = sid.polarity_scores(raw_text)
            mood_score_compounded = mood_score_uncompounded['compound']
            mood_score_compounded_rounded =                 round(mood_score_compounded, 2)
            mood_score_list_.append(mood_score_compounded_rounded)

    min_mood_score_list_ = round(min(mood_score_list_), 4)
    max_mood_score_list_ = round(max(mood_score_list_), 4)

    return (min_mood_score_list_, max_mood_score_list_)


# j,k = mood_score_min_max()

# print('mood score: min=', j, ',', 'max=', k)

(mood_score_min, mood_score_max) = mood_score_min_max()


def mood_score(song_to_be_scored):

    # https://github.com/cjhutto/vaderSentiment

    sid = SentimentIntensityAnalyzer()
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ''

    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_ + ' '
    mood_score_uncompounded_of_song_to_be_scored =         sid.polarity_scores(raw_text)
    mood_score_compounded_of_song_to_be_scored =         mood_score_uncompounded_of_song_to_be_scored['compound']
    mood_score_compounded_of_song_to_be_scored_rounded =         round(mood_score_compounded_of_song_to_be_scored, 2)

    regularization_step =         (mood_score_compounded_of_song_to_be_scored_rounded
         - mood_score_min) / (mood_score_max - mood_score_min)
    mood_score_compounded_of_song_to_be_scored_rounded_regularized = 1         * regularization_step + 0 * (1 - regularization_step)

    return round(mood_score_compounded_of_song_to_be_scored_rounded_regularized,
                 4)


# l = mood_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('mood score=', l)

def length_score_min_max():

    length_score_list_ = []

    for artist in artists_list():

        for song in artist_s_cleaned_songs_list(artist):

            num_words = 0

            f = open(dir_given + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
            length_score_list_.append(num_words)

    min_length_score_list_ = min(length_score_list_)
    max_length_score_list_ = max(length_score_list_)

    return (min_length_score_list_, max_length_score_list_)


# m,n = length_score_min_max()

# print('length score: min=', m, ',', 'max=', n)

(length_score_min, length_score_max) = length_score_min_max()


def length_score(song_to_be_scored):

    num_words_of_song_to_be_scored = 0
    f = open(dir_given + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        num_words_of_song_to_be_scored += len(this_line_wordlist)

    length_score_of_song_to_be_scored = num_words_of_song_to_be_scored

    regularization_step = (length_score_of_song_to_be_scored
                           - length_score_min) / (length_score_max
                                                  - length_score_min)
    length_score_of_song_to_be_scored_regularized = 1         * regularization_step + 0 * (1 - regularization_step)

    return round(length_score_of_song_to_be_scored_regularized, 2)


# o = length_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('length score=', o)

def complexity_score_min_max():

    complexity_score_list_ = []

    for artist in artists_list():

        for song in artist_s_cleaned_songs_list(artist):

            num_words = 0
            words_of_lyrics = []

            f = open(dir_given() + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
                for word_ in this_line_wordlist:
                    words_of_lyrics.append(word_)

            filtered_words = [word for word in words_of_lyrics if word
                              not in stopwords.words('english')
                              and len(word) > 1 and word not in ['na',
                                                                 'la']]  # remove the stopwords
            unique_number_of_words = len(set(filtered_words))
            number_of_words = len(words_of_lyrics)
            try:
                complexity_score = unique_number_of_words                     / number_of_words
                complexity_score = round(complexity_score, 2)
                complexity_score_list_.append(complexity_score)
            except ZeroDivisionError:
                complexity_score = 0
                complexity_score = round(complexity_score, 2)
                complexity_score_list_.append(complexity_score)

    min_complexity_score_list_ = min(set(complexity_score_list_))
    max_complexity_score_list_ = max(set(complexity_score_list_))

    return (min_complexity_score_list_, max_complexity_score_list_)


# p,q = complexity_score_min_max()

# print('complexity score: min=', p, ',', 'max=', q)

(complexity_score_min, complexity_score_max) =     complexity_score_min_max()


def complexity_score(song_to_be_scored):

    num_words_of_song_to_be_scored = 0
    words_of_lyrics_of_song_to_be_scored = []

    f = open(dir_given() + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        num_words_of_song_to_be_scored += len(this_line_wordlist)
        for word_ in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word_)

    filtered_words_of_song_to_be_scored = [word for word in
                                           words_of_lyrics_of_song_to_be_scored if word
                                           not in stopwords.words('english') and len(word) > 1
                                           and word not in ['na', 'la']]  # remove the stopwords
    unique_number_of_words_of_song_to_be_scored =         len(set(filtered_words_of_song_to_be_scored))
    number_of_words_of_song_to_be_scored =         len(words_of_lyrics_of_song_to_be_scored)
    complexity_score_of_song_to_be_scored =         unique_number_of_words_of_song_to_be_scored         / number_of_words_of_song_to_be_scored
    complexity_score_of_song_to_be_scored =         round(complexity_score_of_song_to_be_scored, 2)

    regularization_step = (complexity_score_of_song_to_be_scored
                           - complexity_score_min) \
        / (complexity_score_max - complexity_score_min)
    complexity_score_of_song_to_be_scored_regularized = 1         * regularization_step + 0 * (1 - regularization_step)

    return round(complexity_score_of_song_to_be_scored_regularized, 2)


# r = complexity_score('cleaned_688~I Wanna Be Loved~Buy This Song.txt')

# print('complexity score=', r)


# In[ ]:


# FINALL!!!

# def song_cleaning():
#     try:
#         os.mkdir(dir_given + '/Cleaned_Songs/')
#     except FileExistsError:
#         pass

#     for artist in set(artists_list()):
#         for song in artist_s_songs_list(artist):
#             words_of_lyrics = []
#             fin = open(dir_given + r'/' + song, 'rb')
#             raw_text = ""
#             for line in fin.readlines():    
#                 # remove empty lines
#                 this_line_wordlist = line.decode('utf-8').split()
#                 for word in this_line_wordlist:
#                     words_of_lyrics.append(word)
#             for word_ in words_of_lyrics:
#                 raw_text += word_+" "
#             # remove identifiers like chorus, verse, etc
#             raw_text = re.sub(r"[\(\[].*?[\)\]]", "", raw_text)
#             raw_text = re.sub(r'[\W+]', ' ', raw_text)
#             raw_text = re.sub(r'[\s]', ' ', raw_text)
#             raw_text =  re.sub(r"\b[a-zA-Z]\b", "", raw_text)
#             raw_text = re.sub(' +', ' ', raw_text)
#             fout = open(os.path.join(dir_given +
#                                   '/Cleaned_Songs', 'cleaned_' + song), "wb")
#             fout.write(raw_text.encode('utf-8'))
#             fin.close()
#             fout.close()
#     return
# song_cleaning()


# In[30]:


def artist_s_cleaned_songs_list(str) -> list:
    artist_s_cleaned_songs_list_ = []
    for cleaned_raw_filename in os.listdir(dir_given + '/Cleaned_Songs/'):
        if str == cleaned_raw_filename.split("~")[1].split(".txt")[0]:
            if cleaned_raw_filename not in artist_s_cleaned_songs_list_:
                artist_s_cleaned_songs_list_.append(cleaned_raw_filename)
    return artist_s_cleaned_songs_list_

for element in artist_s_cleaned_songs_list('The-Beatles'):
    print(element)
    


# In[ ]:





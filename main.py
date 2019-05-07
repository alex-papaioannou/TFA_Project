#!/usr/bin/env python
# coding: utf-8

import uuid
import requests
from googletrans import Translator
import argparse
from profanity_check import predict, predict_prob
import nltk.data
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import os.path
import os
import re
import time
import pip
import subprocess
from langdetect import detect
from mtranslate import translate


def pip_install(package):
    subprocess.call(['pip', 'install', package])


pip_install('nltk')
nltk.downloader.download('vader_lexicon')
nltk.downloader.download('stopwords')

pip_install('profanity-check')

pip_install('coverage')
pip_install('langdetect')
#from langdetect import detect

pip_install('googletrans')
translator = Translator()

pip_install('mtranslate')


def dir_given(test_var=0):
    try:
        ret = dir_given_arg
    except:
        ret = test_var
    return ret

# Make a list of all the artists


def artists_list(*args)->list:
    artists_list_ = []
    for raw_filename in os.listdir(dir_given(*args)):
        if raw_filename.endswith('.txt'):
            try:
                artist_name = raw_filename.split("~")[1].split(".txt")[0]
                if artist_name not in artists_list_:
                    artists_list_.append(artist_name)
            except IndexError:
                pass
    return artists_list_

# Make a list of the raw filenames


def raw_filenames_list(*args)->list:
    raw_filenames_list_ = []
    for raw_filename in os.listdir(dir_given(*args)):
        if raw_filename.endswith('.txt'):
            raw_filenames_list_.append(raw_filename)
    return raw_filenames_list_

# For any given artist, return a list of their songs


def artist_s_songs_list(str, *args)->list:
    artist_s_songs_list_ = []
    for raw_filename in raw_filenames_list(*args):
        if str in raw_filename:
            artist_s_songs_list_.append(raw_filename)
    return artist_s_songs_list_

# Remove uneeded characters from the songs


def song_cleaning(*args):
    try:
        os.mkdir(dir_given(*args) + '/Cleaned_Songs')
    except FileExistsError:
        pass

    for artist in set(artists_list(*args)):
        for song in artist_s_songs_list(artist, *args):
            f = open(dir_given(*args) + r'/' + song, 'rb')
            all_words = ''
            for sentence in f.readlines():
                this_sentence = sentence.decode('utf-8')
                all_words += this_sentence
            # remove identifiers like chorus, verse, etc
            all_words = re.sub(r'[\(\[],.*?[\)\]]', '', all_words)
            # remove empty lines
            all_words = os.linesep.join(
                [s for s in all_words.splitlines() if s])
            f.close()
            f = open(os.path.join(dir_given(*args) +
                                  '/Cleaned_Songs', 'cleaned_' + song), "wb")
            f.write(all_words.encode('utf-8'))
            f.close()
    return

# Given an artist, return a list of their cleaned songs


def artist_s_cleaned_songs_list(str, *args)->list:
    artist_s_cleaned_songs_list_ = []
    for cleaned_raw_filename in os.listdir(dir_given(*args) + '/Cleaned_Songs/'):
        if str in cleaned_raw_filename:
            artist_s_cleaned_songs_list_.append(cleaned_raw_filename)
    return artist_s_cleaned_songs_list_


def id_song_to_be_scored(song_to_be_scored):
    pattern = re.compile(
        r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<song_title>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        id_ = match.group('id')
        return int(id_)
    except:
        pass


def artist_song_to_be_scored(song_to_be_scored):
    pattern = re.compile(
        r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        artist_ = match.group('artist_name').replace('-', ' ')
        return artist_
    except:
        pass


def title_song_to_be_scored(song_to_be_scored):
    pattern = re.compile(
        r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)')
    match = pattern.match(song_to_be_scored)
    try:
        song_title_ = match.group('song_title').replace('-', ' ')
        return song_title_
    except:
        pass

# Using pprofanity check to determine profanity in songs


def profanity_score_min_max(*args):
    profanity_score_list_ = []
    for artist in set(artists_list(*args)):
        for song in artist_s_cleaned_songs_list(artist, *args):
            words_of_lyrics = []
            raw_text = ""
            f = open(dir_given(*args) + '/Cleaned_Songs/' + song, 'rb')
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
#            print(profanity_score)

    min_profanity_score_list_ = round(min(profanity_score_list_), 2)
    max_profanity_score_list_ = round(max(profanity_score_list_), 2)

    return min_profanity_score_list_, max_profanity_score_list_


def profanity_score(song_to_be_scored, profanity_score_min, profanity_score_max, *args):
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ""

    f = open(dir_given(*args) + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        for word in this_line_wordlist:
            words_of_lyrics_of_song_to_be_scored.append(word)
    for word_ in words_of_lyrics_of_song_to_be_scored:
        raw_text += word_+" "

    song_lyrics_for_profanity_check_of_song_to_be_scored = [raw_text]
    profanity_check = predict_prob(
        song_lyrics_for_profanity_check_of_song_to_be_scored)
    profanity_score_of_song_to_be_scored = 1 - \
        float(' '.join(map(str, profanity_check)))

    regularization_step = (profanity_score_of_song_to_be_scored -
                           profanity_score_min)/(profanity_score_max - profanity_score_min)
    profanity_score_of_song_to_be_scored_regularized = 1 * \
        regularization_step + 0*(1-regularization_step)

    return round(profanity_score_of_song_to_be_scored_regularized, 2)

# How many words in a song correlate to "Loving" words


def love_score_min_max(*args):
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

    for artist in set(artists_list(*args)):

        for song in artist_s_cleaned_songs_list(artist, *args):
            words_of_lyrics = []
            with open(dir_given(*args) + '/Cleaned_Songs/' + song, 'rb') as f:
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
                love_score = counter_for_love_words/len(filtered_words)
                love_score_rounded = round(love_score, 4)
                love_score_list_.append(love_score_rounded)

    min_love_score_list_ = round(min(love_score_list_), 4)
    max_love_score_list_ = round(max(love_score_list_), 4)
#     print("Love MinMax Time:", time.time() - love_minmax_time)

    return min_love_score_list_, max_love_score_list_


def love_score(song_to_be_scored, love_score_min, love_score_max, *args):

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
    f = open(dir_given(*args) + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
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
    love_score_of_song_to_be_scored = counter_for_love_words / \
        len(filtered_words)
    love_score_of_song_to_be_scored_rounded = round(
        love_score_of_song_to_be_scored, 4)

    regularization_step = (love_score_of_song_to_be_scored_rounded -
                           love_score_min)/(love_score_max - love_score_min)
    love_score_of_song_to_be_scored_rounded_regularized = 1 * \
        regularization_step + 0*(1-regularization_step)

    return round(love_score_of_song_to_be_scored_rounded_regularized, 2)

# Using a sentiment analyzer to determine the positivity, negativity, and neutrality of a song


def mood_score_min_max(*args)->float:

    sid = SentimentIntensityAnalyzer()
    mood_score_list_ = []

    for artist in set(artists_list(*args)):

        for song in artist_s_cleaned_songs_list(artist, *args):
            words_of_lyrics = []
            raw_text = ""
            f = open(dir_given(*args) + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                for word in this_line_wordlist:
                    words_of_lyrics.append(word)
            for word_ in words_of_lyrics:
                raw_text += word_+" "
            mood_score_uncompounded = sid.polarity_scores(raw_text)
            mood_score_compounded = mood_score_uncompounded['compound']
            mood_score_compounded_rounded = round(mood_score_compounded, 2)
            mood_score_list_.append(mood_score_compounded_rounded)

    min_mood_score_list_ = round(min(mood_score_list_), 4)
    max_mood_score_list_ = round(max(mood_score_list_), 4)

    return min_mood_score_list_, max_mood_score_list_


def mood_score(song_to_be_scored, mood_score_min, mood_score_max, *args)->float:

    sid = SentimentIntensityAnalyzer()
    words_of_lyrics_of_song_to_be_scored = []
    raw_text = ""

    f = open(dir_given(*args) + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
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
        mood_score_compounded_of_song_to_be_scored, 2)

    regularization_step = (mood_score_compounded_of_song_to_be_scored_rounded -
                           mood_score_min)/(mood_score_max - mood_score_min)
    mood_score_compounded_of_song_to_be_scored_rounded_regularized = 1 * \
        regularization_step + 0*(1-regularization_step)

    return round(mood_score_compounded_of_song_to_be_scored_rounded_regularized, 4)

# Total number of words


def length_score_min_max(*args):

    length_score_list_ = []

    for artist in set(artists_list(*args)):
        for song in artist_s_cleaned_songs_list(artist, *args):

            num_words = 0

            f = open(dir_given(*args) + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
            length_score_list_.append(num_words)

    min_length_score_list_ = min(length_score_list_)
    max_length_score_list_ = max(length_score_list_)

    return min_length_score_list_, max_length_score_list_


def length_score(song_to_be_scored, length_score_min, length_score_max, *args):

    num_words_of_song_to_be_scored = 0
    f = open(dir_given(*args) + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
    for line in f.readlines():
        this_line_wordlist = line.decode('utf-8').split()
        num_words_of_song_to_be_scored += len(this_line_wordlist)

    length_score_of_song_to_be_scored = num_words_of_song_to_be_scored

    regularization_step = (length_score_of_song_to_be_scored -
                           length_score_min)/(length_score_max - length_score_min)
    length_score_of_song_to_be_scored_regularized = 1 * \
        regularization_step + 0*(1-regularization_step)

    return round(length_score_of_song_to_be_scored_regularized, 2)

# How many unique words a song contains


def complexity_score_min_max(*args):

    complexity_score_list_ = []

    for artist in set(artists_list(*args)):
        for song in artist_s_cleaned_songs_list(artist, *args):

            num_words = 0
            words_of_lyrics = []

            f = open(dir_given(*args) + '/Cleaned_Songs/' + song, 'rb')
            for line in f.readlines():
                this_line_wordlist = line.decode('utf-8').split()
                num_words += len(this_line_wordlist)
                for word_ in this_line_wordlist:
                    words_of_lyrics.append(word_)

            filtered_words = [word for word in words_of_lyrics if word not in stopwords.words(
                'english') and len(word) > 1 and word not in ['na', 'la']]  # remove the stopwords
            unique_number_of_words = len(set(filtered_words))
            number_of_words = len(words_of_lyrics)
            complexity_score = unique_number_of_words/number_of_words
            complexity_score = round(complexity_score, 2)
            complexity_score_list_.append(complexity_score)

    min_complexity_score_list_ = min(set(complexity_score_list_))
    max_complexity_score_list_ = max(set(complexity_score_list_))

    return min_complexity_score_list_, max_complexity_score_list_


def complexity_score(song_to_be_scored, complexity_score_min, complexity_score_max, *args):

    num_words_of_song_to_be_scored = 0
    words_of_lyrics_of_song_to_be_scored = []

    f = open(dir_given(*args) + '/Cleaned_Songs/' + song_to_be_scored, 'rb')
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
    complexity_score_of_song_to_be_scored = unique_number_of_words_of_song_to_be_scored / \
        number_of_words_of_song_to_be_scored
    complexity_score_of_song_to_be_scored = round(
        complexity_score_of_song_to_be_scored, 2)

    regularization_step = (complexity_score_of_song_to_be_scored -
                           complexity_score_min)/(complexity_score_max - complexity_score_min)
    complexity_score_of_song_to_be_scored_regularized = 1 * \
        regularization_step + 0*(1-regularization_step)

    return round(complexity_score_of_song_to_be_scored_regularized, 2)


def json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max, *args):
    dict_for_json = {}
    counter_j = 0
    for song in os.listdir(dir_given(*args) + '/Cleaned_Songs/'):
        counter_j += 1
        dict_for_json_song = {}
        dict_for_json_song["id"] = id_song_to_be_scored(song)
        dict_for_json_song["artist"] = artist_song_to_be_scored(song)
        dict_for_json_song["title"] = title_song_to_be_scored(song)
        if translator.detect(title_song_to_be_scored(song)).lang != 'en':
            dict_for_json_song["kids_safe"] = 0.5
            dict_for_json_song["love"] = 0.5
            dict_for_json_song["mood"] = 0.5
        else:
            dict_for_json_song["kids_safe"] = profanity_score(
                song, profanity_score_min, profanity_score_max)
            dict_for_json_song["love"] = love_score(
                song, love_score_min, love_score_max)
            dict_for_json_song["mood"] = mood_score(
                song, mood_score_min, mood_score_max)
        dict_for_json_song["length"] = length_score(
            song, length_score_min, length_score_max)
        dict_for_json_song["complexity"] = complexity_score(
            song, complexity_score_min, complexity_score_max)
        dict_for_json.setdefault('characterizations:',
                                 []).append(dict_for_json_song)

#             , ensure_ascii = False
    print(json.dumps(dict_for_json, indent=4))


def main():
    artists_list_ = artists_list()
#     print("Artist Time:", time.time() - start_time)

    raw_filenames_list_ = raw_filenames_list()
    song_cleaning()
#     print("Ceaning Time:", time.time() - start_time)

    profanity_score_min, profanity_score_max = profanity_score_min_max()
    love_score_min, love_score_max = love_score_min_max()
    mood_score_min, mood_score_max = mood_score_min_max()
    length_score_min, length_score_max = length_score_min_max()
    complexity_score_min, complexity_score_max = complexity_score_min_max()
#     print("MinMax Time:", time.time() - start_time)

    json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max,
                  mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max)


if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser('Parses the given directory of lyrics')
    parser.add_argument('dir_given', help='Directory of the lyrics')
    args = parser.parse_args()

    dir_given_arg = args.dir_given

    os.chdir(dir_given())
    main()
#     print("Runtime is:", time.time() - start_time)
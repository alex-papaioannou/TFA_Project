# IEOR 4501 - TOOLS FOR ANALYTICS
# Final Project

Final Project is a Python project that is submitted as one of the requirements for the fullfillment of the Columbia University IEOR department’s course named “IEOR 4501 - TOOLS FOR ANALYTICS”. The authors of this project are Papaioannou Alexandros Anastasios and Shipley Kyle

## Installation 

### Needed packages

googletrans==2.4.0

```bash

pip install autopep8
pip install coverage
pip install nltk
pip install profanity-check
pip install langdetect
pip install googletrans
pip install requests
pip install pipreqs

```

## Usage

### Environment setting

```python

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

from profanity_check import predict, predict_prob
# https://github.com/vzhou842/profanity-check

import argparse

from langdetect import detect

from googletrans import Translator
translator = Translator()

import requests, uuid
```

### Functions usage

```python

1. artists_list() 

# returns a list with the unique set of artists that are associated with the lyrics text 
# files 
```

```python
2. raw_filenames_list() 

# returns a list with all the filenames of the lyrics text files of the folder named “Lyrics”
```

```python
3. artist_s_songs_list(str)  

# returns a list with all the filenames of the the lyrics text files that are associated with 
# the artist that is passed as a string (str) to the function

i.e. artist_s_songs_list('The Beatles') 

# print(artist_s_songs_list('The Beatles')) returns ['860~Get Back~The Beatles.txt', '629~From Me to You~The Beatles.txt']
```

```python
4. song_cleaning() 

# a) returns a directory under the current (working) directory named "Cleaned_Songs"
# b) iterates through all the lyrics text files of the songs of all the artists of 
#    the artists_list()
# c) opens their lyrics text files of each song, decodes the words in 'utf-8', and cleans 
#    them up by removing special characters and empty lines [\(\[],.*?[\)\]]
# d) creates a new lyrics text file named 'cleaned_<song_name.txt>' for each song 
     and it pastes the cleaned text of the lyrics in the text file 

i.e. the use of that function is just song_cleaning() 

# no positional (*args) or keyword (**kwargs) arguments needed
```
```python
5. artist_s_cleaned_songs_list(str)  

# returns a list with all the filenames of the the “cleaned” lyrics text files that are associated 
# with the artist that is passed as a string (str) to the function

i.e. artist_s_cleaned_songs_list('The Beatles') 

# print(artist_s_cleaned_songs_list('The Beatles')) returns ['cleaned_860~Get Back~The Beatles.txt', 
# 'cleaned_629~From Me to You~The Beatles.txt']
```

```python
6. id_song_to_be_scored(song_to_be_scored) 

# returns the id number of the lyrics text file that is named 'song_to_be_scored' and it is passed as a 
# positional argument -having the data type of a string (str)- to the function.
# Note: regular expressions (regex) has been used in order to capture the id of the song. More, specifically 
# based on the format of the given text files the following pattern was used:
	r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)'

i.e. id_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 

# print(id_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) returns '860'
```

```python
7. artist_song_to_be_scored(song_to_be_scored) 

# returns the name of the artist of the song named 'song_to_be_scored' which is passed as a positional 
# argument -having the data type of a string (str)- to the function
# Note: regular expressions (regex) has been used in order to capture the id of the song. More, specifically 
# based on the format of the given text files the following pattern was used:
	r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)'

i.e. artist_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 

# print(artist_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) returns 'The Beatles'
```
```python
8. title_song_to_be_scored(song_to_be_scored) 

# returns the title of the song named 'song_to_be_scored' which is passed as a positional argument 
# -having the data type of a string (str)- to the function
# Note: regular expressions (regex) has been used in order to capture the id of the song. More, specifically 
# based on the format of the given text files the following pattern was used:
	r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)'
		
i.e. title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 

# print(title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) returns 'Get Back'
```
```python
9. profanity_score_min_max() 

# returns the minimum and maximum value of the profanity (kids_safe) scores based on the scores of the 
# lyrics text files we have been provided with (in the folder named “Lyrics”)
			       
i.e. title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 

# print(title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) returns 'Get Back'				      
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would 
like to change.

Please make sure to update tests as appropriate.

## License
[Alexandros Papaioannou](https://www.linkedin.com/in/apapaio/)
[Kyle Shipley]

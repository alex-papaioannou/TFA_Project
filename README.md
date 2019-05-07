# IEOR 4501 - TOOLS FOR ANALYTICS
# Final Project

## Project Description 

Final Project is a Python project that is submitted as one of the requirements for the fullfillment of the Columbia University IEOR department’s course named “IEOR 4501 - TOOLS FOR ANALYTICS”. The authors of this project are:

1) Papaioannou Alexandros Anastasios
2) Shipley Kyle

## Project Scope 

We were given a set of text files which held music lyrics; each file held a different song’s lyrics. The scope of this project was to create a tool to categorize the songs based on their lyrics. 

Our program constitutes a single python file (.py file) and it is executable as a single command. 
### Input of the program
The input to your command should be the path to the directory holding the song files. 
### Output of the program
The output of your command is a JSON object (sent to standard out, StdOut) that contains a list of characterizations; one for each song. Each characterization object has the listed dimensions (keys) and a values for how well the song fits into that dimension. 

Dimensions


kid_safe: no bad words

0 is not kid safe

1 is very kid safe


love: is it a love song? 

0 is not a love song

1 is a love song


mood: Upbeat, has a positive message

0 is a dark song

1 is a very happy song


length: how long is it

0 is a short song

1 is a very long song


complexity: requires high level of vocabulary to understand

0 is a very simple song: [i.e. this is a very simple song](https://www.youtube.com/watch?v=EdMTl9zHQ9Y)

1 is a very complex song


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

The files of the project are the following: 

1) main.py            , the executable code
2) tests.py           , the unit testing code
3) requirements.txt   , the packages that the projects requires to be installed for the code to be able to run
4) README.md          , the current README file

## Prerequisites

### Required modules:

langdetect==1.0.7

mstranslate==1.1


mtranslate==1.6

profanity_check==1.0.2

requests==2.21.0 

nltk==3.4 


pipreqs==0.4.9 

coverage==4.5.3 

autopep8==1.4.4 

pep8==1.7.1 

```bash
This is how you can install the required modules:

pip install langdetect
pip install mtranslate

pip install profanity-check
pip install requests
pip install nltk

pip install pipreqs
pip install coverage
pip install autopep8
pip install pep8
```

### Environment setting

```python

import os
import os.path
import glob
import re
import json
import time
import argparse
from collections import defaultdict
from collections import Counter
import uuid

from langdetect import detect
from mtranslate import translate

from profanity_check import predict, predict_prob
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk.data
nltk.downloader.download('vader_lexicon')
nltk.downloader.download('stopwords')
```

## Usage

### Functions usage

1. artists_list() 

Returns a list with the unique set of artists that are associated with the lyrics text 
files 

2. raw_filenames_list() 

Returns a list with all the filenames of the lyrics text files of the folder named “Lyrics”


3. artist_s_songs_list(str)  


Returns a list with all the filenames of the the lyrics text files that are associated with 
the artist that is passed as a string (str) to the function

i.e. 

```python

artist_s_songs_list('The Beatles') 

print(artist_s_songs_list('The Beatles')) 
```
returns 
```python

['860~Get Back~The Beatles.txt', '629~From Me to You~The Beatles.txt']
```
4. song_cleaning() 


a) returns a directory under the current (working) directory named "Cleaned_Songs"
b) iterates through all the lyrics text files of the songs of all the artists of 
    the artists_list()
c) opens their lyrics text files of each song, decodes the words in 'utf-8', and cleans 
    them up by removing special characters and empty lines [\(\[],.*?[\)\]]
d) creates a new lyrics text file named 'cleaned_<song_name.txt>' for each song 
     and it pastes the cleaned text of the lyrics in the text file 

i.e. the use of that function is just 
```python
song_cleaning() 
```

no positional (*args) or keyword (**kwargs) arguments needed

5. artist_s_cleaned_songs_list(str)  

returns a list with all the filenames of the the “cleaned” lyrics text files that are associated 
with the artist that is passed as a string (str) to the function

i.e. 

```python

artist_s_cleaned_songs_list('The Beatles') 

print(artist_s_cleaned_songs_list('The Beatles')) 

```
returns 

```python
['cleaned_860~Get Back~The Beatles.txt', 'cleaned_629~From Me to You~The Beatles.txt']

```

6. id_song_to_be_scored(song_to_be_scored) 

Returns the id number of the lyrics text file that is named 'song_to_be_scored' and it is passed as a 
positional argument -having the data type of a string (str)- to the function.
Note: regular expressions (regex) has been used in order to capture the id of the song. More, specifically 
based on the format of the given text files the following pattern was used:

```python
	r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)'
```
i.e. 
```python
id_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 
print(id_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt'))
```
returns 
```python
'860'
```
7. artist_song_to_be_scored(song_to_be_scored) 

Returns the name of the artist of the song named 'song_to_be_scored' which is passed as a positional 
argument -having the data type of a string (str)- to the function
Note: regular expressions (regex) has been used in order to capture the id of the song. More, specifically 
based on the format of the given text files the following pattern was used:
```python
	r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)'
```
i.e. 
```python
artist_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 
print(artist_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) 
```
returns 
```python
'The Beatles'
```

8. title_song_to_be_scored(song_to_be_scored) 

Returns the title of the song named 'song_to_be_scored' which is passed as a positional argument 
-having the data type of a string (str)- to the function
Note: regular expressions (regex) has been used in order to capture the id of the song. More, specifically 
based on the format of the given text files the following pattern was used:
```python

	r'(cleaned_)(?P<id>[\d\D]+)(~)(?P<artist_name>[\d\D]+)(~)(?P<song_title>[\d\D]+)(.txt)'
```
i.e. 
```python
title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt') 
print(title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) 
```
returns 
```python
'Get Back'
```

9. profanity_score_min_max() 

Returns the minimum and maximum value of the profanity (kids_safe) scores based on the scores of the 
lyrics text files we have been provided with (in the folder named “Lyrics”)
			       
i.e. the use of that function is just 
```python
profanity_score_min_max() 
```
no positional (*args) or keyword (**kwargs) arguments needed			      

10. profanity_score(song_to_be_scored)

Returns the normalized (based on the minimum and maximum value calculated of the sample space) profanity 
(kids_safe) score of the song named 'song_to_be_scored' which is passed as a positional argument 
-having the data type of a string (str)- to the function
			       
i.e. 
```python
profanity_score('cleaned_860~Get Back~The Beatles.txt') 
print(title_song_to_be_scored('cleaned_860~Get Back~The Beatles.txt')) returns ''				      
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would 
like to change.

Please make sure to update tests as appropriate.

## License
[Alexandros Papaioannou](https://www.linkedin.com/in/apapaio/)
[Kyle Shipley]

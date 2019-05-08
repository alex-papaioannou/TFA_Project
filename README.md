https://travis-ci.org/apapaioannou92/TFA_Project.svg?branch=master [![Coverage Status](https://coveralls.io/repos/github/apapaioannou92/TFA_Project/badge.svg?branch=master)](https://coveralls.io/github/apapaioannou92/TFA_Project?branch=master)

IEOR 4501 - TOOLS FOR ANALYTICS
====================================
# Final Project

Copyright (c) 2019 [Papaioannou Alexandros](https://www.linkedin.com/in/apapaio/) (aap2204), Shipley Kyle (kss2170). All rights reserved.

See the end of this file for further copyright and license information.

## Table of Contents

- [Project Description](#Project-Description)
- [Project Scope](#Project-Scope)
- [Input of the program](#Input-of-the-program)
- [Output of the program](#Output-of-the-program)
- [Getting Started](#Getting-Started)
- [Prerequisites](#Prerequisites)
- [Required modules](#Required-modules)
- [Environment setting](#Environment-setting)
- [Run](#Run)
- [The source code](#The-source-code)
- [The unit testing code](#The-unit-testing-code)
- [Usage](#Usage)
- [Functions usage](#Functions-usage)
- [Proposals for enhancement](#Proposals-for-enhancement)
- [Copyright and License Information](#Copyright-and-License-Information)
- [Acknowledgments](#Acknowledgments)
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


* kid_safe: no bad words

0 is not kid safe

1 is very kid safe


* love: is it a love song? 

0 is not a love song

1 is a love song


* mood: Upbeat, has a positive message

0 is a dark song

1 is a very happy song


* length: how long is it

0 is a short song

1 is a very long song


* complexity: requires high level of vocabulary to understand

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

## Required modules

* langdetect==1.0.7

* mstranslate==1.1


* mtranslate==1.6

* profanity_check==1.0.2

* requests==2.21.0 

* nltk==3.4 


* pipreqs==0.4.9 

* coverage==4.5.3 

* autopep8==1.4.4 

* pep8==1.7.1 

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
## Run


### The source code


This is accomplished by typing in a bash terminal 

```bash
python main.py <directory_of_the_lyrics_folder>
```
and the report is obtained by running
```bash
python main.py /Users/alex/Downloads/Final_Project/Lyrics
```

### The unit testing code


This is accomplished by typing in a bash terminal 

```bash
python coverage run tests.py
```
i.e.
```bash
python coverage report -m
```

## Usage

### Functions usage

1. artists_list(*args) 

Returns a list with the unique set of artists that are associated with the lyrics text 
files 

i.e. the use of that function is just 

***All functions with \*args only use these arguments to pass a testing directory path 
during testing, when running tests.py***

```python
artists_list() 
```

no positional (*args) or keyword (**kwargs) arguments needed

2. raw_filenames_list(*args) 

Returns a list with all the filenames of the lyrics text files of the folder named “Lyrics”

i.e. the use of that function is just 

```python
raw_filenames_list() 
```

no positional (*args) or keyword (**kwargs) arguments needed


3. artist_s_songs_list(str, *args)  


Returns a list with all the filenames of the the lyrics text files that are associated with 
the artist that is passed as a string (str) to the function

i.e. 

```python

artist_s_songs_list('The-Beatles') 

```
returns 
```python

['629~The-Beatles~From-Me-to-You.txt', '860~The-Beatles~Get-Back.txt']
```
4. song_cleaning(*args) 


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

5. artist_s_cleaned_songs_list(str, *args)  

returns a list with all the filenames of the the “cleaned” lyrics text files that are associated 
with the artist that is passed as a string (str) to the function

i.e. 

```python

artist_s_cleaned_songs_list('The-Beatles') 

```
returns 

```python

['cleaned_860~The-Beatles~Get-Back.txt', 'cleaned_629~The-Beatles~From-Me-to-You.txt']

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

id_song_to_be_scored('cleaned_860~The-Beatles~Get-Back.txt') 

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

artist_song_to_be_scored('cleaned_860~The-Beatles~Get-Back.txt') 

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

title_song_to_be_scored('cleaned_860~The-Beatles~Get-Back.txt') 

```
returns 

```python

'Get Back'

```

9. profanity_score_min_max(*args) 

Returns the minimum and maximum value of the profanity (kids_safe) scores based on the scores of the 
lyrics text files we have been provided with (in the folder named “Lyrics”)
			       
i.e. the use of that function is just 
```python
profanity_score_min_max() 
```
no positional (*args) or keyword (**kwargs) arguments needed			      

returns 

```python

(0.0, 1.0)

```

10. profanity_score(song_to_be_scored, *args)

Returns the normalized (based on the minimum and maximum value calculated of the sample space) profanity 
(kids_safe) score of the song named 'song_to_be_scored' which is passed as a positional argument 
-having the data type of a string (str)- to the function
			       
i.e. 
```python
profanity_score('cleaned_860~The-Beatles~Get-Back.txt') 
```
returns 
```python
1.0				      
```

11. love_score_min_max(*args) 

Returns the minimum and maximum value of the love scores based on the scores of the 
lyrics text files we have been provided with (in the folder named “Lyrics”)
			       
i.e. the use of that function is just 
```python
love_score_min_max() 
```
no positional (*args) or keyword (**kwargs) arguments needed			      

returns 

```python

(0.0, 1.909)

```
12. love_score(song_to_be_scored, *args)

Returns the normalized (based on the minimum and maximum value calculated of the sample space) love 
score of the song named 'song_to_be_scored' which is passed as a positional argument 
-having the data type of a string (str)- to the function
			       
i.e. 

```python

love_score('cleaned_860~The-Beatles~Get-Back.txt') 

```
returns 

```python

0.0				      

```

13. mood_score_min_max(*args) 

Returns the minimum and maximum value of the mood scores (has positive is the song's message) 
based on the scores of the lyrics text files we have been provided with (in the folder named 
“Lyrics”)
			       
i.e. the use of that function is just 
```python
mood_score_min_max() 
```
no positional (*args) or keyword (**kwargs) arguments needed			      

returns 

```python

(-0.999, 1.0)

```
14. mood_score(song_to_be_scored, *args)

Returns the normalized (based on the minimum and maximum value calculated of the sample space) mood 
score of the song named 'song_to_be_scored' which is passed as a positional argument -having the data 
type of a string (str)- to the function
			       
i.e. 

```python

mood_score('cleaned_860~The-Beatles~Get-Back.txt') 

```

returns 

```python

0.6				      

```

15. length_score_min_max(*args) 

Returns the minimum and maximum value of the length scores (how long a song is) based on the scores 
of the lyrics text files we have been provided with (in the folder named “Lyrics”)
			       
i.e. the use of that function is just 
```python
length_score_min_max() 
```
no positional (*args) or keyword (**kwargs) arguments needed			      

returns 

```python

(0, 961)

```
16. length_score(song_to_be_scored, *args)

Returns the normalized (based on the minimum and maximum value calculated of the sample space) length 
score of the song named 'song_to_be_scored' which is passed as a positional argument -having the data 
type of a string (str)- to the function
			       
i.e. 

```python

length_score('cleaned_860~The-Beatles~Get-Back.txt') 

```

returns 

```python

0.2				      

```

17. complexity_score_min_max(*args) 

Returns the minimum and maximum value of the complexity scores (how complex a song is) based on the scores 
of the lyrics text files we have been provided with (in the folder named “Lyrics”)
			       
i.e. the use of that function is just 

```python

complexity_score_min_max() 

```

no positional (*args) or keyword (**kwargs) arguments needed			      

returns 

```python

(0, 1.0)

```
18. complexity_score(song_to_be_scored, *args)

Returns the normalized (based on the minimum and maximum value calculated of the sample space) complexity
score of the song named 'song_to_be_scored' which is passed as a positional argument -having the data 
type of a string (str)- to the function
			       
i.e. 

```python

complexity_score('cleaned_860~The-Beatles~Get-Back.txt') 

```

returns 

```python

0.2				      

```

19. json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max, *args)

Returns the output of the program; a JSON object (sent to standard out, StdOut) that contains a list of characterizations; 
one for each song. Each characterization object has the listed dimensions (keys) and a values for how well the song fits 
into that dimension. These values have been normalized based on the min and max values of the sample space of each specific dimension. The positional arguments passed in the function named json_creation() are:

* artists_list_
* raw_filenames_list_
* profanity_score_min
* profanity_score_max
* love_score_min
* love_score_max
* mood_score_min
* mood_score_max
* length_score_min
* length_score_max
* complexity_score_min
* complexity_score_max
		       
i.e. 
```python
json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max)
print(json_creation(artists_list_, raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max))
```
returns 
```python
{
    "characterizations:": [
        {
            "id": 873,
            "artist": "Jerry Keller",
            "title": "Here Comes Summer",
            "kids_safe": 1.0,
            "love": 0.12,
            "mood": 1.0,
            "length": 0.25,
            "complexity": 0.38
        },
        {
            "id": 797,
            "artist": "Alexandre Poulin",
            "title": "R\u00eave de Ti Cul",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.31,
            "complexity": 0.69
        },
        {
            "id": 245,
            "artist": "BMR4",
            "title": "Fixing a Hole",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.025,
            "length": 0.17,
            "complexity": 0.28
        },
        {
            "id": 889,
            "artist": "Donnie McClurkin",
            "title": "Just for Me",
            "kids_safe": 0.99,
            "love": 0.32,
            "mood": 0.995,
            "length": 0.14,
            "complexity": 0.43
        },
        {
            "id": 23,
            "artist": "Vin\u00edcius de Moraes",
            "title": "Samba Em Prel\u00fadio",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.11,
            "complexity": 0.64
        },
        {
            "id": 60,
            "artist": "Grateful Dead",
            "title": "Viola Lee Blues",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.87,
            "length": 0.1,
            "complexity": 0.36
        },
        {
            "id": 875,
            "artist": "Chuck Wagon Gang",
            "title": "A Beautiful Life",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.54,
            "length": 0.3,
            "complexity": 0.28
        },
        {
            "id": 830,
            "artist": "Tanya Tucker",
            "title": "It's a Little Too Late",
            "kids_safe": 0.95,
            "love": 0.1,
            "mood": 0.845,
            "length": 0.27,
            "complexity": 0.15
        },
        {
            "id": 731,
            "artist": "The Marshall Tucker Band",
            "title": "Hillbilly Band",
            "kids_safe": 0.67,
            "love": 0.09,
            "mood": 0.93,
            "length": 0.15,
            "complexity": 0.4
        },
        {
            "id": 635,
            "artist": "Sheppard",
            "title": "Geronimo",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.33,
            "complexity": 0.24
        },
        {
            "id": 634,
            "artist": "OneRepublic",
            "title": "I Lived",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.84,
            "length": 0.26,
            "complexity": 0.24
        },
        {
            "id": 323,
            "artist": "Dakota",
            "title": "Life in a Northern Town",
            "kids_safe": 0.2,
            "love": 0.0,
            "mood": 0.96,
            "length": 0.25,
            "complexity": 0.35
        },
        {
            "id": 450,
            "artist": "Rox",
            "title": "No Going Back",
            "kids_safe": 0.75,
            "love": 0.04,
            "mood": 0.075,
            "length": 0.43,
            "complexity": 0.24
        },
        {
            "id": 233,
            "artist": "The McGuire Sisters",
            "title": "Sugartime",
            "kids_safe": 1.0,
            "love": 0.37,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.2
        },
        {
            "id": 537,
            "artist": "Bryon Garrison",
            "title": "I Had the Craziest Dream",
            "kids_safe": 0.85,
            "love": 0.19,
            "mood": 0.985,
            "length": 0.12,
            "complexity": 0.46
        },
        {
            "id": 30,
            "artist": "Doctor Wu Rock & Soul Revue",
            "title": "Can't Turn You Loose",
            "kids_safe": 0.11,
            "love": 0.12,
            "mood": 1.0,
            "length": 0.36,
            "complexity": 0.15
        },
        {
            "id": 39,
            "artist": "Elton John",
            "title": "Street Boogie",
            "kids_safe": 0.76,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.15,
            "complexity": 0.38
        },
        {
            "id": 650,
            "artist": "Bloc Party",
            "title": "Helicopter",
            "kids_safe": 0.37,
            "love": 0.03,
            "mood": 1.0,
            "length": 0.25,
            "complexity": 0.35
        },
        {
            "id": 344,
            "artist": "Atlanta Rhythm Section",
            "title": "Silver Eagle",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.375,
            "length": 0.11,
            "complexity": 0.53
        },
        {
            "id": 402,
            "artist": "Delta Goodrem",
            "title": "Born To Try",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.16,
            "complexity": 0.25
        },
        {
            "id": 933,
            "artist": "Debbie Reynolds",
            "title": "Am I That Easy to Forget?",
            "kids_safe": 0.97,
            "love": 0.21,
            "mood": 0.99,
            "length": 0.12,
            "complexity": 0.35
        },
        {
            "id": 70,
            "artist": "The Beta Band",
            "title": "Broke",
            "kids_safe": 0.98,
            "love": 0.1,
            "mood": 0.855,
            "length": 0.07,
            "complexity": 0.45
        },
        {
            "id": 856,
            "artist": "Jimmy Reed",
            "title": "Baby What You Want Me to Do",
            "kids_safe": 0.37,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.11,
            "complexity": 0.13
        },
        {
            "id": 520,
            "artist": "The Veronicas",
            "title": "4ever",
            "kids_safe": 0.08,
            "love": 0.25,
            "mood": 0.91,
            "length": 0.37,
            "complexity": 0.19
        },
        {
            "id": 411,
            "artist": "Gregory Porter",
            "title": "1960 What? [Opolopo Kick and Bass Rerub]",
            "kids_safe": 0.0,
            "love": 0.04,
            "mood": 0.995,
            "length": 0.38,
            "complexity": 0.24
        },
        {
            "id": 71,
            "artist": "Rollins Band",
            "title": "Do It",
            "kids_safe": 0.02,
            "love": 0.0,
            "mood": 0.7,
            "length": 0.18,
            "complexity": 0.11
        },
        {
            "id": 804,
            "artist": "Migos",
            "title": "Migos Origin",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.035,
            "length": 0.71,
            "complexity": 0.38
        },
        {
            "id": 857,
            "artist": "I Am Kloot",
            "title": "Over My Shoulder",
            "kids_safe": 0.01,
            "love": 0.06,
            "mood": 0.715,
            "length": 0.15,
            "complexity": 0.26
        },
        {
            "id": 198,
            "artist": "Blondestreak",
            "title": "Do You Know the Way to San Jose?",
            "kids_safe": 1.0,
            "love": 0.02,
            "mood": 0.98,
            "length": 0.27,
            "complexity": 0.31
        },
        {
            "id": 792,
            "artist": "Michael Cleveland",
            "title": "Miller's Cave",
            "kids_safe": 0.44,
            "love": 0.04,
            "mood": 0.32,
            "length": 0.16,
            "complexity": 0.42
        },
        {
            "id": 24,
            "artist": "Frank Stallone",
            "title": "Far from Over",
            "kids_safe": 0.83,
            "love": 0.0,
            "mood": 0.115,
            "length": 0.12,
            "complexity": 0.24
        },
        {
            "id": 95,
            "artist": "Mikaila",
            "title": "So in Love with Two",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 1.0,
            "length": 0.38,
            "complexity": 0.18
        },
        {
            "id": 86,
            "artist": "The Calvin Milburn Band",
            "title": "Believer",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.965,
            "length": 0.34,
            "complexity": 0.16
        },
        {
            "id": 721,
            "artist": "Raffi",
            "title": "Rise and Shine",
            "kids_safe": 1.0,
            "love": 0.09,
            "mood": 0.99,
            "length": 0.15,
            "complexity": 0.26
        },
        {
            "id": 740,
            "artist": "Tyler Bryant & the Shakedown",
            "title": "Say a Prayer",
            "kids_safe": 0.52,
            "love": 0.0,
            "mood": 0.85,
            "length": 0.23,
            "complexity": 0.24
        },
        {
            "id": 407,
            "artist": "Mario Lanza",
            "title": "Be My Love (from the film The Toast of New Orleans)",
            "kids_safe": 0.99,
            "love": 0.4,
            "mood": 1.0,
            "length": 0.16,
            "complexity": 0.24
        },
        {
            "id": 960,
            "artist": "Avicii",
            "title": "Levels",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.06,
            "complexity": 0.18
        },
        {
            "id": 898,
            "artist": "Generation X",
            "title": "Revenge",
            "kids_safe": 0.02,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.17,
            "complexity": 0.47
        },
        {
            "id": 38,
            "artist": "Blondie",
            "title": "Atomic",
            "kids_safe": 0.63,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.07,
            "complexity": 0.22
        },
        {
            "id": 945,
            "artist": "Altan",
            "title": "Donal Agus Morag",
            "kids_safe": 0.9,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 734,
            "artist": "The Kingston Trio",
            "title": "Tom Dooley",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.31,
            "complexity": 0.22
        },
        {
            "id": 753,
            "artist": "James Lee Stanley",
            "title": "Daydream Believer",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.94,
            "length": 0.12,
            "complexity": 0.46
        },
        {
            "id": 825,
            "artist": "Xzibit",
            "title": "Harder",
            "kids_safe": 0.0,
            "love": 0.05,
            "mood": 0.0,
            "length": 0.71,
            "complexity": 0.42
        },
        {
            "id": 3,
            "artist": "Jeff Beck",
            "title": "All Shook Up",
            "kids_safe": 0.83,
            "love": 0.1,
            "mood": 1.0,
            "length": 0.32,
            "complexity": 0.31
        },
        {
            "id": 437,
            "artist": "Queen",
            "title": "Play the Game",
            "kids_safe": 0.33,
            "love": 0.37,
            "mood": 1.0,
            "length": 0.23,
            "complexity": 0.23
        },
        {
            "id": 863,
            "artist": "Nat King Cole",
            "title": "Mona Lisa",
            "kids_safe": 0.83,
            "love": 0.0,
            "mood": 0.945,
            "length": 0.15,
            "complexity": 0.26
        },
        {
            "id": 66,
            "artist": "Nicolai Dunger",
            "title": "This Town",
            "kids_safe": 0.99,
            "love": 0.22,
            "mood": 0.965,
            "length": 0.16,
            "complexity": 0.41
        },
        {
            "id": 617,
            "artist": "Gigliola Cinquetti",
            "title": "Non Ho l'\u00c9ta",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.235,
            "length": 0.13,
            "complexity": 0.35
        },
        {
            "id": 982,
            "artist": "the Colour Field",
            "title": "Can't Get Enough of You Baby",
            "kids_safe": 0.86,
            "love": 0.22,
            "mood": 0.995,
            "length": 0.25,
            "complexity": 0.14
        },
        {
            "id": 843,
            "artist": "Unknown Mortal Orchestra",
            "title": "Faded in the Morning",
            "kids_safe": 0.64,
            "love": 0.0,
            "mood": 0.085,
            "length": 0.13,
            "complexity": 0.2
        },
        {
            "id": 475,
            "artist": "Fatboy Slim",
            "title": "The Weekend Starts Here",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.28,
            "length": 0.1,
            "complexity": 0.42
        },
        {
            "id": 25,
            "artist": "Young Gunz",
            "title": "Set It Off",
            "kids_safe": 0.07,
            "love": 0.01,
            "mood": 0.02,
            "length": 0.78,
            "complexity": 0.28
        },
        {
            "id": 971,
            "artist": "Carmen McRae",
            "title": "If You Could See Me Now",
            "kids_safe": 0.95,
            "love": 0.21,
            "mood": 0.985,
            "length": 0.13,
            "complexity": 0.43
        },
        {
            "id": 498,
            "artist": "Tina Turner",
            "title": "A Fool In Love",
            "kids_safe": 0.21,
            "love": 0.21,
            "mood": 0.965,
            "length": 0.18,
            "complexity": 0.43
        },
        {
            "id": 150,
            "artist": "Buy This Song",
            "title": "Overture",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.385,
            "length": 0.03,
            "complexity": 0.85
        },
        {
            "id": 764,
            "artist": "Frank Ifield",
            "title": "I Remember You",
            "kids_safe": 0.94,
            "love": 0.12,
            "mood": 0.985,
            "length": 0.13,
            "complexity": 0.29
        },
        {
            "id": 837,
            "artist": "Amy Macdonald",
            "title": "In the End",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.875,
            "length": 0.21,
            "complexity": 0.27
        },
        {
            "id": 140,
            "artist": "Raunchy",
            "title": "The Comfort in Leaving",
            "kids_safe": 0.0,
            "love": 0.07,
            "mood": 0.035,
            "length": 0.2,
            "complexity": 0.4
        },
        {
            "id": 612,
            "artist": "Beny Mor\u00e9",
            "title": "Mambo No. 5",
            "kids_safe": 0.25,
            "love": 0.05,
            "mood": 0.82,
            "length": 0.11,
            "complexity": 0.38
        },
        {
            "id": 648,
            "artist": "Alboucq, Steve Jazz Quartet",
            "title": "Skylark",
            "kids_safe": 1.0,
            "love": 0.2,
            "mood": 0.835,
            "length": 0.16,
            "complexity": 0.39
        },
        {
            "id": 664,
            "artist": "Duke Ellington",
            "title": "Black Butterfly",
            "kids_safe": 0.98,
            "love": 0.08,
            "mood": 0.1,
            "length": 0.17,
            "complexity": 0.25
        },
        {
            "id": 377,
            "artist": "Hatebreed",
            "title": "Idolized and Vilified",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.15,
            "complexity": 0.41
        },
        {
            "id": 729,
            "artist": "Wilbert Harrison",
            "title": "Let's Stick Together",
            "kids_safe": 0.55,
            "love": 0.02,
            "mood": 0.985,
            "length": 0.24,
            "complexity": 0.26
        },
        {
            "id": 962,
            "artist": "Mahalia Jackson",
            "title": "It Came Upon a Midnight Clear",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.19,
            "complexity": 0.61
        },
        {
            "id": 913,
            "artist": "Alejandro Fern\u00e1ndez",
            "title": "Tantita Pena",
            "kids_safe": 0.7,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.27,
            "complexity": 0.25
        },
        {
            "id": 74,
            "artist": "Miriam Makeba",
            "title": "Pata Pata",
            "kids_safe": 0.58,
            "love": 0.0,
            "mood": 0.67,
            "length": 0.1,
            "complexity": 0.35
        },
        {
            "id": 277,
            "artist": "Marvin Gaye",
            "title": "Baby Don't You Do It",
            "kids_safe": 0.86,
            "love": 0.23,
            "mood": 0.995,
            "length": 0.31,
            "complexity": 0.26
        },
        {
            "id": 867,
            "artist": "Neon Blonde",
            "title": "Headlines",
            "kids_safe": 0.17,
            "love": 0.0,
            "mood": 0.04,
            "length": 0.25,
            "complexity": 0.49
        },
        {
            "id": 82,
            "artist": "Georges Brassens",
            "title": "La Mauvaise R\u00e9putation",
            "kids_safe": 0.79,
            "love": 0.0,
            "mood": 0.245,
            "length": 0.31,
            "complexity": 0.39
        },
        {
            "id": 516,
            "artist": "Patsy Cline",
            "title": "Hungry For Love",
            "kids_safe": 0.99,
            "love": 0.41,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.31
        },
        {
            "id": 708,
            "artist": "Billy Joel",
            "title": "My Life",
            "kids_safe": 0.97,
            "love": 0.05,
            "mood": 0.425,
            "length": 0.17,
            "complexity": 0.43
        },
        {
            "id": 85,
            "artist": "Randy Travis",
            "title": "Tonight I'm Playin' Possum [Solo Version] [Version]",
            "kids_safe": 0.45,
            "love": 0.06,
            "mood": 0.99,
            "length": 0.3,
            "complexity": 0.29
        },
        {
            "id": 824,
            "artist": "Nina & Mike",
            "title": "True Love",
            "kids_safe": 0.98,
            "love": 0.86,
            "mood": 0.995,
            "length": 0.08,
            "complexity": 0.16
        },
        {
            "id": 842,
            "artist": "Tommy Sparks",
            "title": "She's Got Me Dancing",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.23,
            "complexity": 0.22
        },
        {
            "id": 559,
            "artist": "Buddy Guy",
            "title": "Broken Hearted Blues",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.18,
            "complexity": 0.33
        },
        {
            "id": 356,
            "artist": "Mary Wells",
            "title": "The One Who Really Loves You",
            "kids_safe": 0.86,
            "love": 0.37,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.35
        },
        {
            "id": 631,
            "artist": "Roger Miller",
            "title": "Don't We All Have the Right",
            "kids_safe": 0.96,
            "love": 0.27,
            "mood": 0.825,
            "length": 0.12,
            "complexity": 0.15
        },
        {
            "id": 328,
            "artist": "Cab Calloway",
            "title": "A Chicken Ain't Nothin' But a Bird",
            "kids_safe": 0.16,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.19,
            "complexity": 0.32
        },
        {
            "id": 908,
            "artist": "Audrey Gallagher",
            "title": "Big Sky",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.25,
            "complexity": 0.14
        },
        {
            "id": 142,
            "artist": "Snap",
            "title": "Snap",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.22,
            "complexity": 0.38
        },
        {
            "id": 185,
            "artist": "Cherri Bomb",
            "title": "Take This Now",
            "kids_safe": 0.42,
            "love": 0.0,
            "mood": 0.6,
            "length": 0.05,
            "complexity": 0.35
        },
        {
            "id": 548,
            "artist": "Kill Creek",
            "title": "Kathleen",
            "kids_safe": 0.74,
            "love": 0.0,
            "mood": 0.425,
            "length": 0.17,
            "complexity": 0.47
        },
        {
            "id": 605,
            "artist": "The Platters",
            "title": "With This Ring",
            "kids_safe": 1.0,
            "love": 0.68,
            "mood": 1.0,
            "length": 0.21,
            "complexity": 0.24
        },
        {
            "id": 975,
            "artist": "Moe Tucker",
            "title": "Danny Boy",
            "kids_safe": 0.65,
            "love": 0.09,
            "mood": 0.79,
            "length": 0.16,
            "complexity": 0.44
        },
        {
            "id": 915,
            "artist": "Benny Goodman & His Orchestra",
            "title": "Shine",
            "kids_safe": 0.99,
            "love": 0.03,
            "mood": 0.975,
            "length": 0.22,
            "complexity": 0.39
        },
        {
            "id": 754,
            "artist": "Cliff Richard",
            "title": "On The Beach",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.84,
            "length": 0.24,
            "complexity": 0.22
        },
        {
            "id": 496,
            "artist": "Nuremberg Symphony Orchestra",
            "title": "High Noon: Theme",
            "kids_safe": 0.01,
            "love": 0.04,
            "mood": 0.615,
            "length": 0.17,
            "complexity": 0.41
        },
        {
            "id": 811,
            "artist": "One Way",
            "title": "Who's Foolin' Who",
            "kids_safe": 0.2,
            "love": 0.04,
            "mood": 0.015,
            "length": 0.41,
            "complexity": 0.14
        },
        {
            "id": 207,
            "artist": "Eric Revis",
            "title": "Lulu's Back in Town",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.865,
            "length": 0.29,
            "complexity": 0.33
        },
        {
            "id": 541,
            "artist": "Louis Armstrong",
            "title": "What a Wonderful World",
            "kids_safe": 0.97,
            "love": 0.06,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.39
        },
        {
            "id": 12,
            "artist": "NOFX",
            "title": "Lori Meyers",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.17,
            "complexity": 0.52
        },
        {
            "id": 7,
            "artist": "Chris Rea",
            "title": "Lucky Day",
            "kids_safe": 0.94,
            "love": 0.12,
            "mood": 0.975,
            "length": 0.1,
            "complexity": 0.52
        },
        {
            "id": 363,
            "artist": "Garou",
            "title": "Gentleman cambrioleur",
            "kids_safe": 0.91,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.19,
            "complexity": 0.37
        },
        {
            "id": 919,
            "artist": "Quireboys",
            "title": "I Don't Love You Anymore",
            "kids_safe": 0.85,
            "love": 0.02,
            "mood": 0.02,
            "length": 0.26,
            "complexity": 0.36
        },
        {
            "id": 433,
            "artist": "Big Joe Turner",
            "title": "Chains of Love",
            "kids_safe": 0.37,
            "love": 0.21,
            "mood": 0.985,
            "length": 0.14,
            "complexity": 0.31
        },
        {
            "id": 582,
            "artist": "Jorge Drexler",
            "title": "Todo Cae",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.6,
            "length": 0.24,
            "complexity": 0.31
        },
        {
            "id": 423,
            "artist": "Don Gibson",
            "title": "Rings of Gold",
            "kids_safe": 0.99,
            "love": 0.14,
            "mood": 0.925,
            "length": 0.1,
            "complexity": 0.43
        },
        {
            "id": 640,
            "artist": "Eddie \"Lockjaw\" Davis",
            "title": "I Only Have Eyes for You",
            "kids_safe": 0.72,
            "love": 0.26,
            "mood": 0.88,
            "length": 0.1,
            "complexity": 0.38
        },
        {
            "id": 973,
            "artist": "Johnny Rivers",
            "title": "Days of Wine and Roses",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.91,
            "length": 0.09,
            "complexity": 0.36
        },
        {
            "id": 139,
            "artist": "Van Morrison",
            "title": "Whenever God Shines His Light",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 0.31,
            "length": 0.38,
            "complexity": 0.24
        },
        {
            "id": 299,
            "artist": "Reba McEntire",
            "title": "It's Your Call",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.89,
            "length": 0.15,
            "complexity": 0.36
        },
        {
            "id": 567,
            "artist": "Mika",
            "title": "Good Guys [Night Time Mix] [*]",
            "kids_safe": 0.51,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.39,
            "complexity": 0.13
        },
        {
            "id": 989,
            "artist": "Art Brut",
            "title": "Nag Nag Nag Nag",
            "kids_safe": 0.52,
            "love": 0.0,
            "mood": 0.015,
            "length": 0.26,
            "complexity": 0.3
        },
        {
            "id": 445,
            "artist": "Sonny Boy Williamson II",
            "title": "Keep It to Yourself",
            "kids_safe": 0.74,
            "love": 0.25,
            "mood": 0.985,
            "length": 0.12,
            "complexity": 0.26
        },
        {
            "id": 626,
            "artist": "Johnny Powers",
            "title": "Rattled",
            "kids_safe": 0.63,
            "love": 0.0,
            "mood": 0.065,
            "length": 0.19,
            "complexity": 0.21
        },
        {
            "id": 966,
            "artist": "Little Richard",
            "title": "Tutti Frutti",
            "kids_safe": 0.34,
            "love": 0.06,
            "mood": 0.98,
            "length": 0.28,
            "complexity": 0.13
        },
        {
            "id": 726,
            "artist": "Buy This Song",
            "title": "That's the Way Love Is",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 1.0,
            "length": 0.35,
            "complexity": 0.25
        },
        {
            "id": 861,
            "artist": "Seal",
            "title": "Knock on Wood",
            "kids_safe": 0.92,
            "love": 0.29,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.32
        },
        {
            "id": 540,
            "artist": "The Exploited",
            "title": "Beat the Bastards",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.24,
            "complexity": 0.14
        },
        {
            "id": 895,
            "artist": "Elis",
            "title": "I Come Undone",
            "kids_safe": 1.0,
            "love": 0.16,
            "mood": 0.915,
            "length": 0.21,
            "complexity": 0.23
        },
        {
            "id": 685,
            "artist": "Frank Sinatra",
            "title": "A Fine Romance",
            "kids_safe": 0.81,
            "love": 0.26,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.44
        },
        {
            "id": 307,
            "artist": "Peter Maffay",
            "title": "Liebe Wird Verboten",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.24,
            "complexity": 0.48
        },
        {
            "id": 483,
            "artist": "Death Cab for Cutie",
            "title": "Stay Young, Go Dancing",
            "kids_safe": 1.0,
            "love": 0.12,
            "mood": 0.95,
            "length": 0.22,
            "complexity": 0.29
        },
        {
            "id": 373,
            "artist": "Zebrahead",
            "title": "HMP",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.41,
            "complexity": 0.3
        },
        {
            "id": 478,
            "artist": "Joe Walsh",
            "title": "Meadows",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.225,
            "length": 0.13,
            "complexity": 0.44
        },
        {
            "id": 63,
            "artist": "The Troggs",
            "title": "Wild Thing",
            "kids_safe": 1.0,
            "love": 0.35,
            "mood": 0.96,
            "length": 0.11,
            "complexity": 0.15
        },
        {
            "id": 980,
            "artist": "Faces",
            "title": "Wicked Messenger",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 0.115,
            "length": 0.17,
            "complexity": 0.42
        },
        {
            "id": 901,
            "artist": "Earl Bostic",
            "title": "Where or When",
            "kids_safe": 0.98,
            "love": 0.1,
            "mood": 0.975,
            "length": 0.09,
            "complexity": 0.33
        },
        {
            "id": 834,
            "artist": "Stan Getz",
            "title": "Don't Get Around Much Anymore",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.735,
            "length": 0.08,
            "complexity": 0.52
        },
        {
            "id": 365,
            "artist": "G.B.H.",
            "title": "Time Bomb",
            "kids_safe": 0.66,
            "love": 0.09,
            "mood": 0.045,
            "length": 0.07,
            "complexity": 0.57
        },
        {
            "id": 839,
            "artist": "Peter Frampton",
            "title": "Verge of a Thing",
            "kids_safe": 0.74,
            "love": 0.0,
            "mood": 0.71,
            "length": 0.22,
            "complexity": 0.22
        },
        {
            "id": 603,
            "artist": "Junior Jack",
            "title": "Thrill Me",
            "kids_safe": 0.88,
            "love": 0.0,
            "mood": 0.805,
            "length": 0.01,
            "complexity": 0.41
        },
        {
            "id": 778,
            "artist": "Eels",
            "title": "Ordinary Man",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.25,
            "length": 0.16,
            "complexity": 0.35
        },
        {
            "id": 155,
            "artist": "Gloria Estefan",
            "title": "Con Los A\u00f1os Que Me Quedan [With the Years That I Have Left]",
            "kids_safe": 0.92,
            "love": 0.0,
            "mood": 0.635,
            "length": 0.24,
            "complexity": 0.43
        },
        {
            "id": 680,
            "artist": "Patsy Cline",
            "title": "Crazy",
            "kids_safe": 0.1,
            "love": 0.06,
            "mood": 0.01,
            "length": 0.1,
            "complexity": 0.39
        },
        {
            "id": 229,
            "artist": "Jack Scott",
            "title": "Burning Bridges",
            "kids_safe": 0.98,
            "love": 0.07,
            "mood": 0.37,
            "length": 0.11,
            "complexity": 0.36
        },
        {
            "id": 871,
            "artist": "Kate Smith",
            "title": "Who Cares?",
            "kids_safe": 0.82,
            "love": 0.43,
            "mood": 0.98,
            "length": 0.05,
            "complexity": 0.47
        },
        {
            "id": 533,
            "artist": "Randy",
            "title": "Chicken Shack",
            "kids_safe": 0.99,
            "love": 0.03,
            "mood": 0.93,
            "length": 0.2,
            "complexity": 0.46
        },
        {
            "id": 221,
            "artist": "Zao",
            "title": "Repressed",
            "kids_safe": 0.86,
            "love": 0.06,
            "mood": 0.97,
            "length": 0.1,
            "complexity": 0.66
        },
        {
            "id": 72,
            "artist": "Grandmaster Flash & the Furious Five",
            "title": "White Lines (Don't Do It)",
            "kids_safe": 0.61,
            "love": 0.02,
            "mood": 0.87,
            "length": 0.62,
            "complexity": 0.32
        },
        {
            "id": 159,
            "artist": "Earl Scruggs",
            "title": "Some of Shelley's Blues",
            "kids_safe": 0.98,
            "love": 0.15,
            "mood": 0.025,
            "length": 0.2,
            "complexity": 0.32
        },
        {
            "id": 579,
            "artist": "Krokus",
            "title": "Down the Drain",
            "kids_safe": 0.15,
            "love": 0.15,
            "mood": 0.01,
            "length": 0.18,
            "complexity": 0.32
        },
        {
            "id": 394,
            "artist": "Stan Kenton & His Orchestra",
            "title": "Peanut Vendor",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.26,
            "complexity": 0.51
        },
        {
            "id": 77,
            "artist": "Ladytron",
            "title": "90 Degrees",
            "kids_safe": 0.94,
            "love": 0.05,
            "mood": 0.955,
            "length": 0.15,
            "complexity": 0.29
        },
        {
            "id": 677,
            "artist": "Dokken",
            "title": "The Hunter",
            "kids_safe": 0.93,
            "love": 0.21,
            "mood": 0.955,
            "length": 0.24,
            "complexity": 0.25
        },
        {
            "id": 55,
            "artist": "St. Paul's Cathedral Choir, London",
            "title": "O Little Town of Bethlehem",
            "kids_safe": 0.63,
            "love": 0.09,
            "mood": 0.96,
            "length": 0.13,
            "complexity": 0.39
        },
        {
            "id": 706,
            "artist": "Ricasso",
            "title": "Guitar Town",
            "kids_safe": 0.94,
            "love": 0.03,
            "mood": 0.535,
            "length": 0.26,
            "complexity": 0.47
        },
        {
            "id": 552,
            "artist": "White Plains",
            "title": "My Baby Loves Lovin'",
            "kids_safe": 1.0,
            "love": 0.56,
            "mood": 1.0,
            "length": 0.29,
            "complexity": 0.16
        },
        {
            "id": 314,
            "artist": "Black Grape",
            "title": "In the Name of the Father",
            "kids_safe": 0.28,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.35,
            "complexity": 0.33
        },
        {
            "id": 739,
            "artist": "Michael Nesmith",
            "title": "Silver Moon",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.18,
            "complexity": 0.3
        },
        {
            "id": 773,
            "artist": "Frank Sinatra",
            "title": "Sentimental Baby",
            "kids_safe": 0.35,
            "love": 0.4,
            "mood": 0.995,
            "length": 0.1,
            "complexity": 0.3
        },
        {
            "id": 345,
            "artist": "Shakira",
            "title": "How Do You Do",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.125,
            "length": 0.42,
            "complexity": 0.23
        },
        {
            "id": 719,
            "artist": "Fleetwood Mac",
            "title": "Homework",
            "kids_safe": 0.52,
            "love": 0.21,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.16
        },
        {
            "id": 705,
            "artist": "Bob Dylan",
            "title": "Mr. Tambourine Man",
            "kids_safe": 0.89,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.46,
            "complexity": 0.32
        },
        {
            "id": 40,
            "artist": "Amy Winehouse",
            "title": "Moody's Mood For Love",
            "kids_safe": 0.12,
            "love": 0.1,
            "mood": 1.0,
            "length": 0.38,
            "complexity": 0.41
        },
        {
            "id": 672,
            "artist": "Matthew West",
            "title": "Day One [Acoustic]",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.43,
            "complexity": 0.24
        },
        {
            "id": 166,
            "artist": "Glen Hansard",
            "title": "Grace Beneath the Pines",
            "kids_safe": 0.73,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.22,
            "complexity": 0.23
        },
        {
            "id": 665,
            "artist": "Craig Duncan and the Smoky Mountain Band",
            "title": "Orange Blossom Special",
            "kids_safe": 0.99,
            "love": 0.05,
            "mood": 0.96,
            "length": 0.14,
            "complexity": 0.33
        },
        {
            "id": 694,
            "artist": "Brian Piper",
            "title": "There Is No Greater Love",
            "kids_safe": 0.99,
            "love": 0.38,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.23
        },
        {
            "id": 406,
            "artist": "Natalie Cole",
            "title": "Sleigh Ride",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 175,
            "artist": "Nat Adderley",
            "title": "I Married an Angel",
            "kids_safe": 1.0,
            "love": 0.68,
            "mood": 1.0,
            "length": 0.18,
            "complexity": 0.25
        },
        {
            "id": 791,
            "artist": "Israel & New Breed",
            "title": "Friend",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 0.94,
            "length": 0.09,
            "complexity": 0.41
        },
        {
            "id": 8,
            "artist": "Sarah Harmer",
            "title": "Almost",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.32
        },
        {
            "id": 146,
            "artist": "Portishead",
            "title": "Silence",
            "kids_safe": 0.79,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.11,
            "complexity": 0.39
        },
        {
            "id": 766,
            "artist": "The Kinks",
            "title": "You Really Got Me",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.24,
            "complexity": 0.06
        },
        {
            "id": 237,
            "artist": "Stereo Total",
            "title": "Chelsea Girls [Thieves Like Us Remix]",
            "kids_safe": 0.48,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.13,
            "complexity": 0.51
        },
        {
            "id": 213,
            "artist": "Buy This Song",
            "title": "Goodnight Sweetheart",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 1.0,
            "length": 0.13,
            "complexity": 0.25
        },
        {
            "id": 165,
            "artist": "Radiohead",
            "title": "You",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.055,
            "length": 0.09,
            "complexity": 0.35
        },
        {
            "id": 583,
            "artist": "Madita",
            "title": "Ceylon",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.93,
            "length": 0.16,
            "complexity": 0.4
        },
        {
            "id": 218,
            "artist": "Van Halen",
            "title": "Eagles Fly",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.675,
            "length": 0.17,
            "complexity": 0.39
        },
        {
            "id": 10,
            "artist": "Foghat",
            "title": "I Just Want To Make Love To You",
            "kids_safe": 0.27,
            "love": 0.29,
            "mood": 0.985,
            "length": 0.19,
            "complexity": 0.15
        },
        {
            "id": 881,
            "artist": "Rock Goddess",
            "title": "Heartache",
            "kids_safe": 0.86,
            "love": 0.18,
            "mood": 0.97,
            "length": 0.2,
            "complexity": 0.37
        },
        {
            "id": 99,
            "artist": "Oscar Peterson",
            "title": "Stella by Starlight",
            "kids_safe": 0.99,
            "love": 0.16,
            "mood": 0.96,
            "length": 0.08,
            "complexity": 0.42
        },
        {
            "id": 32,
            "artist": "Belchior",
            "title": "Mucuripe",
            "kids_safe": 0.76,
            "love": 0.0,
            "mood": 0.6,
            "length": 0.08,
            "complexity": 0.79
        },
        {
            "id": 272,
            "artist": "Jill Corey",
            "title": "Bye Bye Blackbird",
            "kids_safe": 0.95,
            "love": 0.16,
            "mood": 0.99,
            "length": 0.13,
            "complexity": 0.26
        },
        {
            "id": 704,
            "artist": "Fato",
            "title": "Terrenal",
            "kids_safe": 0.92,
            "love": 0.0,
            "mood": 0.235,
            "length": 0.17,
            "complexity": 0.42
        },
        {
            "id": 565,
            "artist": "UCLA Marching Band",
            "title": "Word Up",
            "kids_safe": 0.88,
            "love": 0.12,
            "mood": 0.99,
            "length": 0.38,
            "complexity": 0.23
        },
        {
            "id": 122,
            "artist": "Richard \"Cookie\" Thomas",
            "title": "Hallelujah I Just Love Her So",
            "kids_safe": 0.99,
            "love": 0.15,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.37
        },
        {
            "id": 575,
            "artist": "Panic! At the Disco",
            "title": "From a Mountain in the Middle of the Cabins",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.08,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 497,
            "artist": "The Four Freshmen",
            "title": "I Can't Believe That You're In Love With Me",
            "kids_safe": 1.0,
            "love": 0.42,
            "mood": 1.0,
            "length": 0.27,
            "complexity": 0.26
        },
        {
            "id": 554,
            "artist": "SHeDAISY",
            "title": "Whatever It Takes",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.85,
            "length": 0.18,
            "complexity": 0.38
        },
        {
            "id": 368,
            "artist": "Billy Grammer",
            "title": "Gotta Travel On",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.13,
            "length": 0.16,
            "complexity": 0.39
        },
        {
            "id": 669,
            "artist": "Jean Louis Aubert",
            "title": "Moments",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.19,
            "complexity": 0.43
        },
        {
            "id": 647,
            "artist": "Ligabue",
            "title": "A  Che Ora \u00e8 la Fine del Mondo? [It's the End of the World as We Know It",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.38,
            "complexity": 0.35
        },
        {
            "id": 678,
            "artist": "Paul Kotheimer",
            "title": "Hallelujah, I'm a Bum",
            "kids_safe": 0.98,
            "love": 0.05,
            "mood": 0.955,
            "length": 0.12,
            "complexity": 0.53
        },
        {
            "id": 638,
            "artist": "Jazz Ambassadors",
            "title": "I'll Be Seeing You",
            "kids_safe": 0.99,
            "love": 0.06,
            "mood": 0.89,
            "length": 0.11,
            "complexity": 0.37
        },
        {
            "id": 571,
            "artist": "Dionne Warwick",
            "title": "That's What Friends Are For",
            "kids_safe": 1.0,
            "love": 0.17,
            "mood": 0.99,
            "length": 0.18,
            "complexity": 0.29
        },
        {
            "id": 607,
            "artist": "The Killers",
            "title": "Exitlude",
            "kids_safe": 0.96,
            "love": 0.07,
            "mood": 0.985,
            "length": 0.11,
            "complexity": 0.37
        },
        {
            "id": 569,
            "artist": "Evans, Bill Trio",
            "title": "My Foolish Heart",
            "kids_safe": 0.65,
            "love": 0.51,
            "mood": 0.985,
            "length": 0.11,
            "complexity": 0.48
        },
        {
            "id": 788,
            "artist": "Lea Salonga",
            "title": "The Last Night Of The World",
            "kids_safe": 0.99,
            "love": 0.06,
            "mood": 0.965,
            "length": 0.27,
            "complexity": 0.3
        },
        {
            "id": 925,
            "artist": "Rex Harrison",
            "title": "Why can't the English",
            "kids_safe": 0.97,
            "love": 0.02,
            "mood": 0.005,
            "length": 0.41,
            "complexity": 0.48
        },
        {
            "id": 938,
            "artist": "Bang Tango",
            "title": "Someone Like You",
            "kids_safe": 0.92,
            "love": 0.0,
            "mood": 0.885,
            "length": 0.23,
            "complexity": 0.28
        },
        {
            "id": 428,
            "artist": "Los Andariegos",
            "title": "No Te Olvidare",
            "kids_safe": 0.69,
            "love": 0.0,
            "mood": 0.235,
            "length": 0.19,
            "complexity": 0.27
        },
        {
            "id": 817,
            "artist": "Daryl Hall & John Oates",
            "title": "Angelina",
            "kids_safe": 0.36,
            "love": 0.24,
            "mood": 0.99,
            "length": 0.16,
            "complexity": 0.29
        },
        {
            "id": 167,
            "artist": "Rita Wilson",
            "title": "River",
            "kids_safe": 1.0,
            "love": 0.09,
            "mood": 0.995,
            "length": 0.24,
            "complexity": 0.27
        },
        {
            "id": 336,
            "artist": "Q",
            "title": "Just Another Day",
            "kids_safe": 0.73,
            "love": 0.01,
            "mood": 0.98,
            "length": 0.51,
            "complexity": 0.45
        },
        {
            "id": 0,
            "artist": "Jerry Harrison",
            "title": "No More Reruns",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 0.045,
            "length": 0.38,
            "complexity": 0.33
        },
        {
            "id": 56,
            "artist": "Malastrana",
            "title": "Runnin' with the Devil",
            "kids_safe": 0.01,
            "love": 0.13,
            "mood": 0.015,
            "length": 0.16,
            "complexity": 0.34
        },
        {
            "id": 480,
            "artist": "Gio",
            "title": "E Menina (Hey Girl)",
            "kids_safe": 0.71,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.08,
            "complexity": 0.2
        },
        {
            "id": 538,
            "artist": "Shark Island",
            "title": "Temptation",
            "kids_safe": 0.03,
            "love": 0.15,
            "mood": 0.92,
            "length": 0.11,
            "complexity": 0.28
        },
        {
            "id": 239,
            "artist": "Wallace Roney",
            "title": "Just My Imagination",
            "kids_safe": 0.8,
            "love": 0.1,
            "mood": 0.325,
            "length": 0.24,
            "complexity": 0.32
        },
        {
            "id": 19,
            "artist": "Buy This Song",
            "title": "Im Grunen Irgendwo",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.59
        },
        {
            "id": 470,
            "artist": "Burl Ives",
            "title": "Rudolph, the Red Nosed Reindeer",
            "kids_safe": 0.36,
            "love": 0.06,
            "mood": 0.995,
            "length": 0.21,
            "complexity": 0.27
        },
        {
            "id": 542,
            "artist": "Napalm Death",
            "title": "Diatribes",
            "kids_safe": 0.87,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.16,
            "complexity": 0.44
        },
        {
            "id": 512,
            "artist": "Jim Bransky",
            "title": "Lady Be Good",
            "kids_safe": 0.91,
            "love": 0.05,
            "mood": 0.99,
            "length": 0.14,
            "complexity": 0.36
        },
        {
            "id": 698,
            "artist": "Anne Murray",
            "title": "Time Don't Run Out on Me",
            "kids_safe": 0.98,
            "love": 0.03,
            "mood": 0.135,
            "length": 0.28,
            "complexity": 0.23
        },
        {
            "id": 320,
            "artist": "Sammy Kershaw",
            "title": "Me and Maxine",
            "kids_safe": 0.47,
            "love": 0.11,
            "mood": 0.93,
            "length": 0.25,
            "complexity": 0.33
        },
        {
            "id": 125,
            "artist": "Haste the Day",
            "title": "Needles",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.14,
            "complexity": 0.31
        },
        {
            "id": 891,
            "artist": "Soul Survivors",
            "title": "Expressway to Your Heart",
            "kids_safe": 0.99,
            "love": 0.2,
            "mood": 0.625,
            "length": 0.21,
            "complexity": 0.31
        },
        {
            "id": 2,
            "artist": "Stanley Clarke",
            "title": "Old Friends",
            "kids_safe": 1.0,
            "love": 0.12,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.31
        },
        {
            "id": 51,
            "artist": "Luis Miguel",
            "title": "Amor de Escuela",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.84,
            "length": 0.14,
            "complexity": 0.53
        },
        {
            "id": 9,
            "artist": "Savoy Hotel Orpheans",
            "title": "Laura",
            "kids_safe": 0.96,
            "love": 0.24,
            "mood": 0.865,
            "length": 0.06,
            "complexity": 0.48
        },
        {
            "id": 943,
            "artist": "Anne Farnsworth",
            "title": "Moondance",
            "kids_safe": 0.95,
            "love": 0.21,
            "mood": 1.0,
            "length": 0.37,
            "complexity": 0.22
        },
        {
            "id": 180,
            "artist": "Vic Dickenson",
            "title": "Dear Old Southland",
            "kids_safe": 0.93,
            "love": 0.18,
            "mood": 0.845,
            "length": 0.04,
            "complexity": 0.36
        },
        {
            "id": 701,
            "artist": "Leigh Stephens",
            "title": "We Gotta Get out of This Place",
            "kids_safe": 0.55,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.29,
            "complexity": 0.25
        },
        {
            "id": 815,
            "artist": "Beyonc\u00e9",
            "title": "Blue",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.95,
            "length": 0.28,
            "complexity": 0.19
        },
        {
            "id": 127,
            "artist": "Vera Lynn",
            "title": "White Cliffs of Dover",
            "kids_safe": 0.76,
            "love": 0.04,
            "mood": 0.975,
            "length": 0.15,
            "complexity": 0.38
        },
        {
            "id": 274,
            "artist": "Tommy Torres",
            "title": "Por un Beso Tuyo",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.11,
            "length": 0.28,
            "complexity": 0.44
        },
        {
            "id": 193,
            "artist": "The Barking Dogs",
            "title": "It's Alright",
            "kids_safe": 0.99,
            "love": 0.03,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.31
        },
        {
            "id": 545,
            "artist": "Sam Chatmon",
            "title": "St. Louis Blues",
            "kids_safe": 0.88,
            "love": 0.28,
            "mood": 0.985,
            "length": 0.14,
            "complexity": 0.43
        },
        {
            "id": 641,
            "artist": "Mark Trichka",
            "title": "Begin The Beguine",
            "kids_safe": 0.99,
            "love": 0.18,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.38
        },
        {
            "id": 878,
            "artist": "Marco Masini",
            "title": "Raccontami di Te",
            "kids_safe": 0.6,
            "love": 0.0,
            "mood": 0.18,
            "length": 0.22,
            "complexity": 0.61
        },
        {
            "id": 270,
            "artist": "Bert Kaempfert & His Orchestra",
            "title": "Whispering",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.2,
            "complexity": 0.22
        },
        {
            "id": 649,
            "artist": "Thomas Dolby",
            "title": "She Blinded Me With Science",
            "kids_safe": 1.0,
            "love": 0.11,
            "mood": 0.995,
            "length": 0.25,
            "complexity": 0.27
        },
        {
            "id": 636,
            "artist": "Jerry Lee Lewis",
            "title": "Carry Me Back to Old Virginia",
            "kids_safe": 0.74,
            "love": 0.08,
            "mood": 0.99,
            "length": 0.21,
            "complexity": 0.21
        },
        {
            "id": 593,
            "artist": "Genesis",
            "title": "Watcher of the Skies",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.035,
            "length": 0.2,
            "complexity": 0.43
        },
        {
            "id": 206,
            "artist": "The Tremble Kids",
            "title": "Embraceable You",
            "kids_safe": 0.78,
            "love": 0.36,
            "mood": 0.975,
            "length": 0.07,
            "complexity": 0.48
        },
        {
            "id": 534,
            "artist": "Tony Joe White",
            "title": "Stud Spider",
            "kids_safe": 0.22,
            "love": 0.03,
            "mood": 0.965,
            "length": 0.27,
            "complexity": 0.33
        },
        {
            "id": 476,
            "artist": "James Blunt",
            "title": "High",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.91,
            "length": 0.17,
            "complexity": 0.37
        },
        {
            "id": 351,
            "artist": "Buy This Song",
            "title": "Firefly",
            "kids_safe": 0.84,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.32
        },
        {
            "id": 768,
            "artist": "The Who",
            "title": "Overture",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.385,
            "length": 0.03,
            "complexity": 0.61
        },
        {
            "id": 546,
            "artist": "Jimmy Johnson",
            "title": "Something You Got",
            "kids_safe": 0.95,
            "love": 0.16,
            "mood": 0.96,
            "length": 0.11,
            "complexity": 0.23
        },
        {
            "id": 131,
            "artist": "Art Blakey",
            "title": "Night In Tunisia",
            "kids_safe": 0.89,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.0,
            "complexity": 1.0
        },
        {
            "id": 67,
            "artist": "Fred Waring & His Pennsylvanians",
            "title": "Little White Lies",
            "kids_safe": 0.13,
            "love": 0.05,
            "mood": 0.005,
            "length": 0.14,
            "complexity": 0.25
        },
        {
            "id": 49,
            "artist": "Negative Approach",
            "title": "Nothing",
            "kids_safe": 0.0,
            "love": 0.18,
            "mood": 0.995,
            "length": 0.36,
            "complexity": 0.15
        },
        {
            "id": 985,
            "artist": "Rod McKuen",
            "title": "Jean",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.885,
            "length": 0.15,
            "complexity": 0.36
        },
        {
            "id": 983,
            "artist": "Thelonious Monk",
            "title": "Just You, Just Me [#]",
            "kids_safe": 0.92,
            "love": 0.0,
            "mood": 0.315,
            "length": 0.05,
            "complexity": 0.57
        },
        {
            "id": 88,
            "artist": "Thievery Corporation",
            "title": "Lebanese Blonde",
            "kids_safe": 0.91,
            "love": 0.03,
            "mood": 0.205,
            "length": 0.2,
            "complexity": 0.22
        },
        {
            "id": 178,
            "artist": "R.E.M.",
            "title": "Kohoutek",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.16,
            "complexity": 0.33
        },
        {
            "id": 847,
            "artist": "Geri Halliwell",
            "title": "Love Never Loved Me",
            "kids_safe": 1.0,
            "love": 0.53,
            "mood": 1.0,
            "length": 0.35,
            "complexity": 0.21
        },
        {
            "id": 179,
            "artist": "Rubberneck",
            "title": "Twisted",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.24,
            "complexity": 0.25
        },
        {
            "id": 367,
            "artist": "Cornelio Reyna",
            "title": "Me Cai de La Nube",
            "kids_safe": 0.9,
            "love": 0.0,
            "mood": 0.235,
            "length": 0.18,
            "complexity": 0.41
        },
        {
            "id": 370,
            "artist": "Crosby & Nash",
            "title": "Half Your Angels",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.885,
            "length": 0.21,
            "complexity": 0.28
        },
        {
            "id": 805,
            "artist": "Boogie Boys",
            "title": "A Fly Girl",
            "kids_safe": 0.72,
            "love": 0.02,
            "mood": 1.0,
            "length": 0.66,
            "complexity": 0.42
        },
        {
            "id": 961,
            "artist": "Jerry Vale",
            "title": "The Song Is You",
            "kids_safe": 1.0,
            "love": 0.2,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.44
        },
        {
            "id": 595,
            "artist": "Thirty Seconds to Mars",
            "title": "Savior",
            "kids_safe": 0.38,
            "love": 0.24,
            "mood": 0.0,
            "length": 0.2,
            "complexity": 0.2
        },
        {
            "id": 376,
            "artist": "Jethro Tull",
            "title": "Grace",
            "kids_safe": 0.94,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.01,
            "complexity": 0.52
        },
        {
            "id": 890,
            "artist": "Jarabe de Palo",
            "title": "Somos",
            "kids_safe": 0.34,
            "love": 0.0,
            "mood": 0.045,
            "length": 0.49,
            "complexity": 0.39
        },
        {
            "id": 238,
            "artist": "Common",
            "title": "The Game",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.65,
            "complexity": 0.36
        },
        {
            "id": 398,
            "artist": "Christopher Cross",
            "title": "No Time for Talk",
            "kids_safe": 0.99,
            "love": 0.12,
            "mood": 0.85,
            "length": 0.13,
            "complexity": 0.45
        },
        {
            "id": 494,
            "artist": "Smiley Lewis",
            "title": "When Did You Leave Heaven",
            "kids_safe": 1.0,
            "love": 0.11,
            "mood": 0.985,
            "length": 0.18,
            "complexity": 0.3
        },
        {
            "id": 921,
            "artist": "JimBo Whaley",
            "title": "Summer of '69",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 0.99,
            "length": 0.28,
            "complexity": 0.36
        },
        {
            "id": 619,
            "artist": "Louis Armstrong",
            "title": "Trees",
            "kids_safe": 0.97,
            "love": 0.23,
            "mood": 0.96,
            "length": 0.09,
            "complexity": 0.55
        },
        {
            "id": 334,
            "artist": "Dr. Feelgood",
            "title": "Johnny B Goode",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.22,
            "complexity": 0.42
        },
        {
            "id": 472,
            "artist": "Buy This Song",
            "title": "He's Funny That Way",
            "kids_safe": 0.47,
            "love": 0.05,
            "mood": 0.995,
            "length": 0.3,
            "complexity": 0.38
        },
        {
            "id": 115,
            "artist": "David Lee Roth",
            "title": "Coconut Grove",
            "kids_safe": 0.42,
            "love": 0.0,
            "mood": 0.05,
            "length": 0.11,
            "complexity": 0.61
        },
        {
            "id": 389,
            "artist": "Los Yonic's",
            "title": "Quincea\u00f1era",
            "kids_safe": 0.72,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.17,
            "complexity": 0.6
        },
        {
            "id": 637,
            "artist": "As I Lay Dying",
            "title": "Tear Out My Eyes",
            "kids_safe": 0.7,
            "love": 0.05,
            "mood": 0.16,
            "length": 0.16,
            "complexity": 0.37
        },
        {
            "id": 96,
            "artist": "The Damned",
            "title": "Billy Bad Breaks",
            "kids_safe": 0.82,
            "love": 0.03,
            "mood": 0.0,
            "length": 0.22,
            "complexity": 0.24
        },
        {
            "id": 733,
            "artist": "Delta Spirit",
            "title": "Bushwick Blues [EP Version]",
            "kids_safe": 0.93,
            "love": 0.33,
            "mood": 0.99,
            "length": 0.19,
            "complexity": 0.44
        },
        {
            "id": 523,
            "artist": "Edyta G\u00f3rniak",
            "title": "Anything",
            "kids_safe": 0.93,
            "love": 0.07,
            "mood": 0.915,
            "length": 0.21,
            "complexity": 0.2
        },
        {
            "id": 372,
            "artist": "Alejandro Sanz",
            "title": "Looking for Paradise",
            "kids_safe": 0.8,
            "love": 0.03,
            "mood": 0.995,
            "length": 0.33,
            "complexity": 0.34
        },
        {
            "id": 292,
            "artist": "Percy Faith",
            "title": "Theme from \"A Summer Place\"",
            "kids_safe": 1.0,
            "love": 0.29,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.36
        },
        {
            "id": 968,
            "artist": "Stephen Fearing",
            "title": "The Finest Kind",
            "kids_safe": 0.37,
            "love": 0.07,
            "mood": 0.985,
            "length": 0.2,
            "complexity": 0.41
        },
        {
            "id": 183,
            "artist": "Here We Go Magic",
            "title": "How Do I Know",
            "kids_safe": 0.66,
            "love": 0.18,
            "mood": 0.98,
            "length": 0.22,
            "complexity": 0.28
        },
        {
            "id": 974,
            "artist": "Stereo MC's",
            "title": "Step It Up",
            "kids_safe": 0.26,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.48,
            "complexity": 0.2
        },
        {
            "id": 242,
            "artist": "Dirt Nasty",
            "title": "I Can't Dance",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.15,
            "length": 0.52,
            "complexity": 0.3
        },
        {
            "id": 750,
            "artist": "Buck Clayton's Orchestra",
            "title": "You're My Thrill",
            "kids_safe": 0.79,
            "love": 0.16,
            "mood": 0.93,
            "length": 0.09,
            "complexity": 0.4
        },
        {
            "id": 553,
            "artist": "DMX",
            "title": "Head Up",
            "kids_safe": 0.65,
            "love": 0.11,
            "mood": 0.075,
            "length": 0.39,
            "complexity": 0.37
        },
        {
            "id": 931,
            "artist": "Johnny Rivers",
            "title": "Poor Side of Town",
            "kids_safe": 0.81,
            "love": 0.07,
            "mood": 0.87,
            "length": 0.2,
            "complexity": 0.37
        },
        {
            "id": 386,
            "artist": "Ray McKinley",
            "title": "Chattanooga Choo Choo",
            "kids_safe": 0.83,
            "love": 0.0,
            "mood": 0.95,
            "length": 0.14,
            "complexity": 0.53
        },
        {
            "id": 760,
            "artist": "D:Ream",
            "title": "Things Can Only Get Better",
            "kids_safe": 0.96,
            "love": 0.08,
            "mood": 0.96,
            "length": 0.3,
            "complexity": 0.25
        },
        {
            "id": 200,
            "artist": "Thelonious Monk",
            "title": "'Round Midnight",
            "kids_safe": 1.0,
            "love": 0.18,
            "mood": 0.715,
            "length": 0.12,
            "complexity": 0.56
        },
        {
            "id": 170,
            "artist": "Michel Sardou",
            "title": "Les Ricains",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.12,
            "complexity": 0.57
        },
        {
            "id": 876,
            "artist": "Wilson Pickett",
            "title": "It's All Over",
            "kids_safe": 0.95,
            "love": 0.06,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.34
        },
        {
            "id": 703,
            "artist": "Vach\u00e9, Allan",
            "title": "Just Friends",
            "kids_safe": 0.98,
            "love": 0.4,
            "mood": 0.935,
            "length": 0.05,
            "complexity": 0.49
        },
        {
            "id": 556,
            "artist": "Dakota Moon",
            "title": "My Song",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 0.91,
            "length": 0.17,
            "complexity": 0.42
        },
        {
            "id": 490,
            "artist": "Cedarmont Kids",
            "title": "Old Time Religion",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 1.0,
            "length": 0.35,
            "complexity": 0.04
        },
        {
            "id": 812,
            "artist": "Afta 1",
            "title": "Believe",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.965,
            "length": 0.34,
            "complexity": 0.16
        },
        {
            "id": 606,
            "artist": "The Moody Blues",
            "title": "Nights in White Satin",
            "kids_safe": 0.99,
            "love": 0.64,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.22
        },
        {
            "id": 254,
            "artist": "The Beach Boys",
            "title": "I'm Waiting For the Day",
            "kids_safe": 0.97,
            "love": 0.31,
            "mood": 0.98,
            "length": 0.22,
            "complexity": 0.29
        },
        {
            "id": 780,
            "artist": "Cascada",
            "title": "Independence Day",
            "kids_safe": 0.1,
            "love": 0.14,
            "mood": 0.995,
            "length": 0.63,
            "complexity": 0.26
        },
        {
            "id": 246,
            "artist": "Anne Murray",
            "title": "O Little Town of Bethlehem",
            "kids_safe": 0.63,
            "love": 0.09,
            "mood": 0.96,
            "length": 0.13,
            "complexity": 0.39
        },
        {
            "id": 360,
            "artist": "Fear Factory",
            "title": "Repentance",
            "kids_safe": 0.19,
            "love": 0.0,
            "mood": 0.405,
            "length": 0.08,
            "complexity": 0.41
        },
        {
            "id": 799,
            "artist": "Iron Butterfly",
            "title": "In A Gadda Da Vida",
            "kids_safe": 0.87,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.11,
            "complexity": 0.19
        },
        {
            "id": 324,
            "artist": "Edie Brickell & New Bohemians",
            "title": "Nothing",
            "kids_safe": 0.45,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.09,
            "complexity": 0.49
        },
        {
            "id": 228,
            "artist": "Mekong Delta",
            "title": "The Healer",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.31,
            "complexity": 0.25
        },
        {
            "id": 827,
            "artist": "Howlin' Wolf",
            "title": "How Many More Years",
            "kids_safe": 0.25,
            "love": 0.0,
            "mood": 0.83,
            "length": 0.11,
            "complexity": 0.38
        },
        {
            "id": 550,
            "artist": "Beastie Boys",
            "title": "Jimi",
            "kids_safe": 0.12,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.09,
            "complexity": 0.49
        },
        {
            "id": 128,
            "artist": "Ian Whitcomb & His Dance Band",
            "title": "Riptide",
            "kids_safe": 0.98,
            "love": 0.65,
            "mood": 0.995,
            "length": 0.16,
            "complexity": 0.24
        },
        {
            "id": 822,
            "artist": "Jad Fair",
            "title": "Frankenstein",
            "kids_safe": 0.95,
            "love": 0.05,
            "mood": 0.065,
            "length": 0.44,
            "complexity": 0.31
        },
        {
            "id": 500,
            "artist": "Lil Wayne",
            "title": "Lose It",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.0,
            "length": 0.49,
            "complexity": 0.34
        },
        {
            "id": 214,
            "artist": "Tina Turner",
            "title": "Proud Mary",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.995,
            "length": 0.23,
            "complexity": 0.4
        },
        {
            "id": 80,
            "artist": "Kyle Vincent",
            "title": "It's Too Late",
            "kids_safe": 0.06,
            "love": 0.06,
            "mood": 0.045,
            "length": 0.23,
            "complexity": 0.31
        },
        {
            "id": 34,
            "artist": "Perry Como",
            "title": "It's Impossible",
            "kids_safe": 0.96,
            "love": 0.09,
            "mood": 0.485,
            "length": 0.17,
            "complexity": 0.27
        },
        {
            "id": 836,
            "artist": "Marty Wilde",
            "title": "Teenager In Love",
            "kids_safe": 1.0,
            "love": 0.29,
            "mood": 0.98,
            "length": 0.24,
            "complexity": 0.23
        },
        {
            "id": 687,
            "artist": "Wild Cherry",
            "title": "It's the Same Old Song",
            "kids_safe": 0.74,
            "love": 0.24,
            "mood": 0.995,
            "length": 0.26,
            "complexity": 0.27
        },
        {
            "id": 909,
            "artist": "Big Mama Thornton",
            "title": "I Smell a Rat",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.15,
            "complexity": 0.27
        },
        {
            "id": 577,
            "artist": "Waka Flocka Flame",
            "title": "Round of Applause",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.0,
            "length": 0.7,
            "complexity": 0.27
        },
        {
            "id": 453,
            "artist": "Shaznay Lewis",
            "title": "Dance",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.32,
            "complexity": 0.28
        },
        {
            "id": 225,
            "artist": "Slowdive",
            "title": "Rutti",
            "kids_safe": 0.79,
            "love": 0.07,
            "mood": 0.19,
            "length": 0.1,
            "complexity": 0.21
        },
        {
            "id": 835,
            "artist": "Anita Ward",
            "title": "Ring My Bell",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.985,
            "length": 0.3,
            "complexity": 0.19
        },
        {
            "id": 661,
            "artist": "Gene Autry",
            "title": "Have I Told You Lately That I Love You",
            "kids_safe": 0.99,
            "love": 0.3,
            "mood": 0.995,
            "length": 0.17,
            "complexity": 0.24
        },
        {
            "id": 598,
            "artist": "NOFX",
            "title": "Lori Meyers",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.17,
            "complexity": 0.52
        },
        {
            "id": 90,
            "artist": "Cobra Starship",
            "title": "The City Is at War",
            "kids_safe": 0.11,
            "love": 0.02,
            "mood": 0.16,
            "length": 0.37,
            "complexity": 0.23
        },
        {
            "id": 586,
            "artist": "Tristan Prettyman",
            "title": "Never Say Never",
            "kids_safe": 1.0,
            "love": 0.15,
            "mood": 1.0,
            "length": 0.51,
            "complexity": 0.3
        },
        {
            "id": 502,
            "artist": "Shabba Ranks",
            "title": "Turn It Down",
            "kids_safe": 0.83,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.04,
            "complexity": 0.52
        },
        {
            "id": 224,
            "artist": "William Bell",
            "title": "Every Day Will Be Like A Holiday",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.13,
            "complexity": 0.31
        },
        {
            "id": 325,
            "artist": "Bebel Gilberto",
            "title": "August Day Song",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.865,
            "length": 0.17,
            "complexity": 0.4
        },
        {
            "id": 261,
            "artist": "Jack Pe\u00f1ate",
            "title": "Pull My Heart Away",
            "kids_safe": 0.91,
            "love": 0.19,
            "mood": 0.98,
            "length": 0.26,
            "complexity": 0.24
        },
        {
            "id": 347,
            "artist": "Paula Abdul",
            "title": "The Way That You Love Me",
            "kids_safe": 0.99,
            "love": 0.46,
            "mood": 1.0,
            "length": 0.38,
            "complexity": 0.2
        },
        {
            "id": 153,
            "artist": "Emma Veary",
            "title": "My Little Grass Shack",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.95,
            "length": 0.25,
            "complexity": 0.19
        },
        {
            "id": 777,
            "artist": "Steve Ellis",
            "title": "Everlasting Love",
            "kids_safe": 0.91,
            "love": 0.14,
            "mood": 1.0,
            "length": 0.3,
            "complexity": 0.24
        },
        {
            "id": 886,
            "artist": "Kyoji Yamamoto",
            "title": "River of Time",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.825,
            "length": 0.21,
            "complexity": 0.3
        },
        {
            "id": 93,
            "artist": "Duncan Dhu",
            "title": "Cien Gaviotas",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.025,
            "length": 0.17,
            "complexity": 0.46
        },
        {
            "id": 528,
            "artist": "The Subdudes",
            "title": "Light in Your Eyes",
            "kids_safe": 0.87,
            "love": 0.2,
            "mood": 0.99,
            "length": 0.26,
            "complexity": 0.24
        },
        {
            "id": 855,
            "artist": "James Taylor",
            "title": "How Sweet It is (To Be Loved By You)",
            "kids_safe": 0.95,
            "love": 0.9,
            "mood": 1.0,
            "length": 0.23,
            "complexity": 0.19
        },
        {
            "id": 589,
            "artist": "Clarence Williams",
            "title": "Organ Grinder Blues",
            "kids_safe": 0.97,
            "love": 0.07,
            "mood": 0.665,
            "length": 0.11,
            "complexity": 0.3
        },
        {
            "id": 486,
            "artist": "Ray Charles",
            "title": "Your Cheating Heart",
            "kids_safe": 1.0,
            "love": 0.32,
            "mood": 0.105,
            "length": 0.14,
            "complexity": 0.31
        },
        {
            "id": 844,
            "artist": "Wye Oak",
            "title": "Plains",
            "kids_safe": 0.96,
            "love": 0.04,
            "mood": 0.025,
            "length": 0.15,
            "complexity": 0.52
        },
        {
            "id": 425,
            "artist": "DMX",
            "title": "Angel",
            "kids_safe": 0.99,
            "love": 0.06,
            "mood": 1.0,
            "length": 0.91,
            "complexity": 0.25
        },
        {
            "id": 294,
            "artist": "Bonnie Bramlett",
            "title": "Love Hurts",
            "kids_safe": 0.57,
            "love": 0.33,
            "mood": 0.99,
            "length": 0.13,
            "complexity": 0.4
        },
        {
            "id": 410,
            "artist": "Fleetwood Mac",
            "title": "Angel",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 1.0,
            "length": 0.27,
            "complexity": 0.32
        },
        {
            "id": 15,
            "artist": "Tyga",
            "title": "Rack City",
            "kids_safe": 0.55,
            "love": 0.01,
            "mood": 0.89,
            "length": 0.49,
            "complexity": 0.25
        },
        {
            "id": 487,
            "artist": "The Cataracs",
            "title": "Top of the World",
            "kids_safe": 0.01,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.33,
            "complexity": 0.29
        },
        {
            "id": 113,
            "artist": "Small Faces",
            "title": "Tin Soldier",
            "kids_safe": 0.98,
            "love": 0.1,
            "mood": 0.995,
            "length": 0.24,
            "complexity": 0.33
        },
        {
            "id": 37,
            "artist": "Buy This Song",
            "title": "[Silence]",
            "kids_safe": 0.83,
            "love": 0.09,
            "mood": 0.96,
            "length": 0.33,
            "complexity": 0.23
        },
        {
            "id": 737,
            "artist": "Natalie Imbruglia",
            "title": "Torn",
            "kids_safe": 0.22,
            "love": 0.07,
            "mood": 0.045,
            "length": 0.32,
            "complexity": 0.29
        },
        {
            "id": 967,
            "artist": "Cursive",
            "title": "From the Hips",
            "kids_safe": 0.18,
            "love": 0.0,
            "mood": 0.33,
            "length": 0.24,
            "complexity": 0.36
        },
        {
            "id": 524,
            "artist": "Martina Stoessel",
            "title": "All\u2019alba Sorger\u00f2 [Italian End Credit Version]",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.04,
            "length": 0.23,
            "complexity": 0.54
        },
        {
            "id": 594,
            "artist": "The Association",
            "title": "Look at Me, Look at You",
            "kids_safe": 0.4,
            "love": 0.08,
            "mood": 0.94,
            "length": 0.33,
            "complexity": 0.24
        },
        {
            "id": 900,
            "artist": "VX",
            "title": "Constant",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.965,
            "length": 0.1,
            "complexity": 0.37
        },
        {
            "id": 993,
            "artist": "Dennis Brown",
            "title": "Lips of Wine",
            "kids_safe": 0.61,
            "love": 0.0,
            "mood": 0.355,
            "length": 0.21,
            "complexity": 0.19
        },
        {
            "id": 396,
            "artist": "Fela Kuti & Africa 70",
            "title": "Lady",
            "kids_safe": 0.21,
            "love": 0.0,
            "mood": 0.17,
            "length": 0.29,
            "complexity": 0.16
        },
        {
            "id": 522,
            "artist": "The Dramatics",
            "title": "Whatcha See Is Whatcha Get",
            "kids_safe": 0.99,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.35,
            "complexity": 0.18
        },
        {
            "id": 529,
            "artist": "Krypteria",
            "title": "Victoriam Speramus [Original Album Version]",
            "kids_safe": 0.8,
            "love": 0.0,
            "mood": 0.915,
            "length": 0.19,
            "complexity": 0.34
        },
        {
            "id": 955,
            "artist": "Bun B",
            "title": "Paper Planes",
            "kids_safe": 0.06,
            "love": 0.0,
            "mood": 0.245,
            "length": 0.4,
            "complexity": 0.22
        },
        {
            "id": 614,
            "artist": "Attaque 77",
            "title": "El Jorobadito",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.18,
            "complexity": 0.43
        },
        {
            "id": 772,
            "artist": "Flaming Ember",
            "title": "Spinning Wheel",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.11,
            "complexity": 0.47
        },
        {
            "id": 282,
            "artist": "Ronan Keating",
            "title": "Time After Time",
            "kids_safe": 0.81,
            "love": 0.0,
            "mood": 0.085,
            "length": 0.21,
            "complexity": 0.31
        },
        {
            "id": 625,
            "artist": "Yank Rachell",
            "title": "Rainy Day Blues",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 0.985,
            "length": 0.34,
            "complexity": 0.39
        },
        {
            "id": 749,
            "artist": "Erk Tha Jerk",
            "title": "Mo Money",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.995,
            "length": 0.72,
            "complexity": 0.37
        },
        {
            "id": 236,
            "artist": "JoJo",
            "title": "Note to God",
            "kids_safe": 0.86,
            "love": 0.3,
            "mood": 1.0,
            "length": 0.34,
            "complexity": 0.2
        },
        {
            "id": 234,
            "artist": "Kim Fowley",
            "title": "The Trip",
            "kids_safe": 0.72,
            "love": 0.0,
            "mood": 0.79,
            "length": 0.2,
            "complexity": 0.43
        },
        {
            "id": 177,
            "artist": "Tito Nieves",
            "title": "O Me Voy O Te Vas",
            "kids_safe": 0.88,
            "love": 0.0,
            "mood": 0.955,
            "length": 0.19,
            "complexity": 0.41
        },
        {
            "id": 684,
            "artist": "Deborah Brown",
            "title": "After You've Gone",
            "kids_safe": 0.52,
            "love": 0.09,
            "mood": 0.03,
            "length": 0.21,
            "complexity": 0.36
        },
        {
            "id": 495,
            "artist": "Buy This Song",
            "title": "Timeless",
            "kids_safe": 1.0,
            "love": 0.47,
            "mood": 1.0,
            "length": 0.28,
            "complexity": 0.21
        },
        {
            "id": 632,
            "artist": "Liza Minnelli",
            "title": "You Can Leave Your Hat On",
            "kids_safe": 0.89,
            "love": 0.3,
            "mood": 0.99,
            "length": 0.15,
            "complexity": 0.32
        },
        {
            "id": 756,
            "artist": "Bj\u00f6rk",
            "title": "I Can't Help loving That Man",
            "kids_safe": 0.84,
            "love": 0.28,
            "mood": 0.035,
            "length": 0.09,
            "complexity": 0.4
        },
        {
            "id": 164,
            "artist": "Zac Brown Band",
            "title": "Keep Me in Mind",
            "kids_safe": 0.16,
            "love": 0.22,
            "mood": 0.995,
            "length": 0.28,
            "complexity": 0.25
        },
        {
            "id": 136,
            "artist": "Jack Elliott",
            "title": "Night Herding Song",
            "kids_safe": 0.24,
            "love": 0.0,
            "mood": 0.1,
            "length": 0.07,
            "complexity": 0.57
        },
        {
            "id": 959,
            "artist": "Conjunto Atardecer",
            "title": "Hoja en Blanco",
            "kids_safe": 0.7,
            "love": 0.0,
            "mood": 0.6,
            "length": 0.39,
            "complexity": 0.53
        },
        {
            "id": 717,
            "artist": "El Viejo Paulino y Su Gente Juli\u00e1n Garza",
            "title": "Misa De Cuerpo Presente",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.07,
            "length": 0.16,
            "complexity": 0.63
        },
        {
            "id": 956,
            "artist": "The Human Beinz",
            "title": "Nobody But Me",
            "kids_safe": 0.62,
            "love": 0.0,
            "mood": 0.4,
            "length": 0.18,
            "complexity": 0.18
        },
        {
            "id": 147,
            "artist": "Jacob Miller",
            "title": "Westbound Train",
            "kids_safe": 0.1,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.28,
            "complexity": 0.24
        },
        {
            "id": 761,
            "artist": "T\u00e9l\u00e9phone",
            "title": "La Bombe Humaine",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.65,
            "length": 0.26,
            "complexity": 0.47
        },
        {
            "id": 838,
            "artist": "The Four Seasons",
            "title": "What Child is This",
            "kids_safe": 0.21,
            "love": 0.04,
            "mood": 0.955,
            "length": 0.15,
            "complexity": 0.6
        },
        {
            "id": 596,
            "artist": "Belly",
            "title": "Might Not",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.58,
            "complexity": 0.3
        },
        {
            "id": 255,
            "artist": "Starsailor",
            "title": "Four to the Floor",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 0.94,
            "length": 0.17,
            "complexity": 0.22
        },
        {
            "id": 564,
            "artist": "Charice",
            "title": "In This Song",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.15,
            "length": 0.26,
            "complexity": 0.3
        },
        {
            "id": 560,
            "artist": "Feist",
            "title": "One Evening",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.91,
            "length": 0.14,
            "complexity": 0.38
        },
        {
            "id": 161,
            "artist": "Van Halen",
            "title": "Not Enough",
            "kids_safe": 1.0,
            "love": 0.37,
            "mood": 0.995,
            "length": 0.2,
            "complexity": 0.29
        },
        {
            "id": 33,
            "artist": ".38 Special",
            "title": "Hold On Loosely",
            "kids_safe": 0.09,
            "love": 0.04,
            "mood": 0.645,
            "length": 0.28,
            "complexity": 0.24
        },
        {
            "id": 291,
            "artist": "Ronnie Lane",
            "title": "You Never Can Tell",
            "kids_safe": 0.95,
            "love": 0.03,
            "mood": 0.98,
            "length": 0.2,
            "complexity": 0.4
        },
        {
            "id": 771,
            "artist": "Connie Stevens",
            "title": "Sixteen Reasons",
            "kids_safe": 0.75,
            "love": 0.36,
            "mood": 0.995,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 568,
            "artist": "Michael Bloomfield",
            "title": "Flip, Flop and Fly",
            "kids_safe": 0.01,
            "love": 0.18,
            "mood": 0.925,
            "length": 0.27,
            "complexity": 0.26
        },
        {
            "id": 775,
            "artist": "Them",
            "title": "You Just Can't Win",
            "kids_safe": 0.58,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.17,
            "complexity": 0.37
        },
        {
            "id": 613,
            "artist": "Diana Ross & the Supremes",
            "title": "Will This Be the Day",
            "kids_safe": 0.98,
            "love": 0.4,
            "mood": 0.995,
            "length": 0.14,
            "complexity": 0.42
        },
        {
            "id": 686,
            "artist": "Pitchshifter",
            "title": "Phoenixology",
            "kids_safe": 0.93,
            "love": 0.09,
            "mood": 0.89,
            "length": 0.14,
            "complexity": 0.37
        },
        {
            "id": 188,
            "artist": "Jaheim",
            "title": "Forever",
            "kids_safe": 1.0,
            "love": 0.49,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.3
        },
        {
            "id": 50,
            "artist": "The Fall",
            "title": "Totally Wired",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 0.01,
            "length": 0.22,
            "complexity": 0.31
        },
        {
            "id": 662,
            "artist": "Buy This Song",
            "title": "I'm Through with Love",
            "kids_safe": 0.99,
            "love": 0.51,
            "mood": 0.99,
            "length": 0.13,
            "complexity": 0.38
        },
        {
            "id": 608,
            "artist": "Ronny",
            "title": "Oh, My Darling Caroline",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.16,
            "complexity": 0.46
        },
        {
            "id": 763,
            "artist": "Coldplay",
            "title": "Speed of Sound",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.75,
            "length": 0.32,
            "complexity": 0.28
        },
        {
            "id": 29,
            "artist": "Charlie Robison",
            "title": "Rain",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.385,
            "length": 0.29,
            "complexity": 0.38
        },
        {
            "id": 176,
            "artist": "Jordainares",
            "title": "Kissin' Cousins (No. 2)",
            "kids_safe": 0.16,
            "love": 0.13,
            "mood": 0.96,
            "length": 0.09,
            "complexity": 0.57
        },
        {
            "id": 585,
            "artist": "Club 8",
            "title": "Close to Me",
            "kids_safe": 0.63,
            "love": 0.18,
            "mood": 0.985,
            "length": 0.29,
            "complexity": 0.22
        },
        {
            "id": 896,
            "artist": "Secret Machines",
            "title": "Sad and Lonely",
            "kids_safe": 0.11,
            "love": 0.05,
            "mood": 0.05,
            "length": 0.16,
            "complexity": 0.36
        },
        {
            "id": 864,
            "artist": "Eddie Santiago",
            "title": "Una Nueva Oportunidad",
            "kids_safe": 0.3,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.28,
            "complexity": 0.31
        },
        {
            "id": 658,
            "artist": "Marvin Gaye",
            "title": "After the Dance [Live]",
            "kids_safe": 0.63,
            "love": 0.1,
            "mood": 0.995,
            "length": 0.42,
            "complexity": 0.29
        },
        {
            "id": 424,
            "artist": "Reel Big Fish",
            "title": "We Care",
            "kids_safe": 0.59,
            "love": 0.54,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.26
        },
        {
            "id": 602,
            "artist": "Sean Paul",
            "title": "Temperature",
            "kids_safe": 0.61,
            "love": 0.04,
            "mood": 0.995,
            "length": 0.37,
            "complexity": 0.4
        },
        {
            "id": 152,
            "artist": "Alvaro Torres",
            "title": "Hazme Olvidarla",
            "kids_safe": 0.82,
            "love": 0.0,
            "mood": 0.69,
            "length": 0.14,
            "complexity": 0.59
        },
        {
            "id": 597,
            "artist": "Daniel Ash",
            "title": "Fever",
            "kids_safe": 0.15,
            "love": 0.15,
            "mood": 0.99,
            "length": 0.29,
            "complexity": 0.35
        },
        {
            "id": 160,
            "artist": "Iron Maiden",
            "title": "Hallowed Be Thy Name",
            "kids_safe": 0.98,
            "love": 0.03,
            "mood": 0.9,
            "length": 0.27,
            "complexity": 0.42
        },
        {
            "id": 126,
            "artist": "Fats Waller",
            "title": "Dinah",
            "kids_safe": 0.92,
            "love": 0.1,
            "mood": 0.92,
            "length": 0.19,
            "complexity": 0.34
        },
        {
            "id": 859,
            "artist": "Demi Lovato",
            "title": "Warrior",
            "kids_safe": 0.86,
            "love": 0.0,
            "mood": 0.16,
            "length": 0.31,
            "complexity": 0.27
        },
        {
            "id": 558,
            "artist": "Jonathan Wilson",
            "title": "Valley of the Silver Moon",
            "kids_safe": 0.3,
            "love": 0.0,
            "mood": 0.935,
            "length": 0.16,
            "complexity": 0.28
        },
        {
            "id": 57,
            "artist": "Dinah Washington",
            "title": "Drinking Again",
            "kids_safe": 0.3,
            "love": 0.11,
            "mood": 0.98,
            "length": 0.19,
            "complexity": 0.3
        },
        {
            "id": 484,
            "artist": "Ismael Rivera",
            "title": "Me Tienes Loco",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.4,
            "complexity": 0.2
        },
        {
            "id": 936,
            "artist": "Martin Solveig",
            "title": "Everybody",
            "kids_safe": 0.04,
            "love": 0.0,
            "mood": 0.04,
            "length": 0.13,
            "complexity": 0.35
        },
        {
            "id": 190,
            "artist": "Deep Purple",
            "title": "Wicked Ways",
            "kids_safe": 0.93,
            "love": 0.17,
            "mood": 0.96,
            "length": 0.23,
            "complexity": 0.34
        },
        {
            "id": 491,
            "artist": "Ani DiFranco",
            "title": "What If No One's Watching",
            "kids_safe": 0.55,
            "love": 0.02,
            "mood": 0.01,
            "length": 0.34,
            "complexity": 0.34
        },
        {
            "id": 823,
            "artist": "Lale Andersen",
            "title": "Lili Marleen",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.075,
            "length": 0.24,
            "complexity": 0.51
        },
        {
            "id": 262,
            "artist": "Ibrahim Tatlises",
            "title": "Vur Gitsin Beni",
            "kids_safe": 0.87,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.12,
            "complexity": 0.42
        },
        {
            "id": 621,
            "artist": "Widespread Panic",
            "title": "Chilly Water (Reprise)",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.24,
            "complexity": 0.41
        },
        {
            "id": 991,
            "artist": "Cynthia Manley",
            "title": "Everybody Dance",
            "kids_safe": 1.0,
            "love": 0.16,
            "mood": 0.98,
            "length": 0.14,
            "complexity": 0.49
        },
        {
            "id": 145,
            "artist": "Kathy Mattea",
            "title": "Trouble With Angels",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.29,
            "complexity": 0.2
        },
        {
            "id": 511,
            "artist": "Ronnie Dyson",
            "title": "When You Get Right Down To It",
            "kids_safe": 0.99,
            "love": 0.09,
            "mood": 0.395,
            "length": 0.19,
            "complexity": 0.19
        },
        {
            "id": 700,
            "artist": "Palast Orchester",
            "title": "Sex Bomb",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.27,
            "length": 0.14,
            "complexity": 0.33
        },
        {
            "id": 911,
            "artist": "Toots & the Maytals",
            "title": "Bla Bla Bla",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.565,
            "length": 0.31,
            "complexity": 0.13
        },
        {
            "id": 939,
            "artist": "Bobby Darin",
            "title": "Make Someone Happy",
            "kids_safe": 0.97,
            "love": 0.33,
            "mood": 0.995,
            "length": 0.09,
            "complexity": 0.49
        },
        {
            "id": 431,
            "artist": "Jimmie Noone",
            "title": "Little White Lies",
            "kids_safe": 0.13,
            "love": 0.05,
            "mood": 0.005,
            "length": 0.14,
            "complexity": 0.25
        },
        {
            "id": 831,
            "artist": "Breaking Benjamin",
            "title": "Breakdown",
            "kids_safe": 0.88,
            "love": 0.07,
            "mood": 0.725,
            "length": 0.21,
            "complexity": 0.25
        },
        {
            "id": 109,
            "artist": "Al Green",
            "title": "Precious Lord",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.15,
            "complexity": 0.32
        },
        {
            "id": 492,
            "artist": "The Who",
            "title": "Summertime Blues",
            "kids_safe": 0.08,
            "love": 0.03,
            "mood": 0.975,
            "length": 0.19,
            "complexity": 0.37
        },
        {
            "id": 105,
            "artist": "Chris Thompson",
            "title": "If You Remember Me",
            "kids_safe": 0.98,
            "love": 0.18,
            "mood": 0.99,
            "length": 0.18,
            "complexity": 0.29
        },
        {
            "id": 381,
            "artist": "Jimmy Reed",
            "title": "You Don't Have to Go",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.26,
            "length": 0.09,
            "complexity": 0.39
        },
        {
            "id": 117,
            "artist": "Spike Jones & His City Slickers",
            "title": "Clink, Clink, Another Drink",
            "kids_safe": 0.9,
            "love": 0.0,
            "mood": 0.84,
            "length": 0.16,
            "complexity": 0.49
        },
        {
            "id": 615,
            "artist": "Husky",
            "title": "I'm Not Coming Back",
            "kids_safe": 0.6,
            "love": 0.0,
            "mood": 0.08,
            "length": 0.28,
            "complexity": 0.26
        },
        {
            "id": 442,
            "artist": "Albert King",
            "title": "Call My Job",
            "kids_safe": 0.95,
            "love": 0.08,
            "mood": 0.92,
            "length": 0.1,
            "complexity": 0.26
        },
        {
            "id": 401,
            "artist": "4 the Cause",
            "title": "Stand by Me",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.375,
            "length": 0.16,
            "complexity": 0.25
        },
        {
            "id": 562,
            "artist": "Jimmy Eat World",
            "title": "(Splash) Turn Twist",
            "kids_safe": 0.74,
            "love": 0.04,
            "mood": 0.975,
            "length": 0.2,
            "complexity": 0.22
        },
        {
            "id": 276,
            "artist": "Peaches & Herb",
            "title": "Shake Your Groove Thing",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 0.82,
            "length": 0.33,
            "complexity": 0.23
        },
        {
            "id": 747,
            "artist": "Semaj",
            "title": "Step in the Name of Love",
            "kids_safe": 0.67,
            "love": 0.12,
            "mood": 1.0,
            "length": 0.68,
            "complexity": 0.26
        },
        {
            "id": 673,
            "artist": "Toquinho e Vinicius",
            "title": "A  Tonga Da Mironga Do Kabulet\u00ea",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.17,
            "complexity": 0.28
        },
        {
            "id": 806,
            "artist": "Benita Hill",
            "title": "The Christmas Song",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.11,
            "complexity": 0.62
        },
        {
            "id": 860,
            "artist": "The Beatles",
            "title": "Get Back",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.59,
            "length": 0.18,
            "complexity": 0.19
        },
        {
            "id": 205,
            "artist": "Fats Waller",
            "title": "Two Sleepy People",
            "kids_safe": 0.95,
            "love": 0.15,
            "mood": 0.965,
            "length": 0.13,
            "complexity": 0.41
        },
        {
            "id": 808,
            "artist": "Carlos Gardel",
            "title": "Caminito",
            "kids_safe": 0.76,
            "love": 0.03,
            "mood": 0.93,
            "length": 0.15,
            "complexity": 0.68
        },
        {
            "id": 924,
            "artist": "Willie Nelson",
            "title": "Bright Lights, Big City",
            "kids_safe": 0.73,
            "love": 0.05,
            "mood": 0.995,
            "length": 0.14,
            "complexity": 0.26
        },
        {
            "id": 840,
            "artist": "Big Maybelle",
            "title": "Candy",
            "kids_safe": 0.83,
            "love": 0.46,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.45
        },
        {
            "id": 266,
            "artist": "Jorge Vercillo",
            "title": "Final Feliz",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.08,
            "complexity": 0.69
        },
        {
            "id": 463,
            "artist": "Sandler & Young",
            "title": "Just the Way You Look Tonight",
            "kids_safe": 0.75,
            "love": 0.17,
            "mood": 0.99,
            "length": 0.11,
            "complexity": 0.48
        },
        {
            "id": 902,
            "artist": "B.B. King",
            "title": "That Evil Child",
            "kids_safe": 0.39,
            "love": 0.0,
            "mood": 0.05,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 688,
            "artist": "Buy This Song",
            "title": "I Wanna Be Loved",
            "kids_safe": 0.97,
            "love": 0.45,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.27
        },
        {
            "id": 504,
            "artist": "T.I.",
            "title": "All Gold Everything [*]",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.0,
            "length": 0.79,
            "complexity": 0.37
        },
        {
            "id": 366,
            "artist": "Richie Havens",
            "title": "What's Going On",
            "kids_safe": 0.98,
            "love": 0.03,
            "mood": 0.085,
            "length": 0.2,
            "complexity": 0.37
        },
        {
            "id": 409,
            "artist": "Mar\u00eda Dolores Pradera",
            "title": "El Rosario de Mi Madre",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.29,
            "length": 0.2,
            "complexity": 0.33
        },
        {
            "id": 702,
            "artist": "Webb Pierce",
            "title": "Slowly",
            "kids_safe": 0.81,
            "love": 0.65,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.19
        },
        {
            "id": 479,
            "artist": "Charlie Parker",
            "title": "Cherokee",
            "kids_safe": 0.96,
            "love": 0.18,
            "mood": 0.99,
            "length": 0.06,
            "complexity": 0.65
        },
        {
            "id": 679,
            "artist": "James Brown",
            "title": "I Don't Want Nobody to Give Me Nothing (Open Up the Door, I'll Get It M",
            "kids_safe": 0.39,
            "love": 0.01,
            "mood": 0.985,
            "length": 1.0,
            "complexity": 0.14
        },
        {
            "id": 682,
            "artist": "The Sound",
            "title": "The Fire",
            "kids_safe": 0.9,
            "love": 0.09,
            "mood": 0.995,
            "length": 0.23,
            "complexity": 0.22
        },
        {
            "id": 848,
            "artist": "Art Blakey & the Jazz Messengers",
            "title": "It's Only a Paper Moon",
            "kids_safe": 1.0,
            "love": 0.21,
            "mood": 0.425,
            "length": 0.19,
            "complexity": 0.18
        },
        {
            "id": 782,
            "artist": "Ken Colyer",
            "title": "When I Leave the World Behind",
            "kids_safe": 0.01,
            "love": 0.12,
            "mood": 0.96,
            "length": 0.19,
            "complexity": 0.25
        },
        {
            "id": 27,
            "artist": "The Rolling Stones",
            "title": "Confessin' the Blues",
            "kids_safe": 0.78,
            "love": 0.12,
            "mood": 0.99,
            "length": 0.12,
            "complexity": 0.39
        },
        {
            "id": 353,
            "artist": "Praga Khan",
            "title": "Breakfast in Vegas",
            "kids_safe": 0.18,
            "love": 0.0,
            "mood": 0.025,
            "length": 0.11,
            "complexity": 0.42
        },
        {
            "id": 663,
            "artist": "Nina Simone",
            "title": "My Baby Just Cares for Me",
            "kids_safe": 0.24,
            "love": 0.44,
            "mood": 0.17,
            "length": 0.14,
            "complexity": 0.21
        },
        {
            "id": 620,
            "artist": "Jerry Lee Lewis",
            "title": "When the Saints Go Marchin' In",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.615,
            "length": 0.06,
            "complexity": 0.25
        },
        {
            "id": 751,
            "artist": "Cristy Lane",
            "title": "One Day at a Time",
            "kids_safe": 1.0,
            "love": 0.1,
            "mood": 0.245,
            "length": 0.14,
            "complexity": 0.42
        },
        {
            "id": 17,
            "artist": "Alf",
            "title": "The Party's Over",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.13,
            "complexity": 0.3
        },
        {
            "id": 999,
            "artist": "Elton John",
            "title": "Song for Guy",
            "kids_safe": 0.19,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.03,
            "complexity": 0.07
        },
        {
            "id": 133,
            "artist": "Hagfish",
            "title": "California",
            "kids_safe": 0.19,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.1,
            "complexity": 0.25
        },
        {
            "id": 784,
            "artist": "Falco",
            "title": "Der Kommissar",
            "kids_safe": 0.51,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.43,
            "complexity": 0.44
        },
        {
            "id": 727,
            "artist": "Young Buck",
            "title": "Lose My Mind",
            "kids_safe": 0.0,
            "love": 0.07,
            "mood": 0.455,
            "length": 0.43,
            "complexity": 0.33
        },
        {
            "id": 471,
            "artist": "Steve Vai",
            "title": "Highway Star [*]",
            "kids_safe": 0.09,
            "love": 0.09,
            "mood": 0.985,
            "length": 0.26,
            "complexity": 0.23
        },
        {
            "id": 412,
            "artist": "Lonestar",
            "title": "Let Me Love You",
            "kids_safe": 0.42,
            "love": 0.23,
            "mood": 0.995,
            "length": 0.3,
            "complexity": 0.19
        },
        {
            "id": 929,
            "artist": "The Oak Ridge Boys",
            "title": "It Takes a Little Rain (To Make Love Grow)",
            "kids_safe": 0.98,
            "love": 0.37,
            "mood": 0.995,
            "length": 0.14,
            "complexity": 0.37
        },
        {
            "id": 539,
            "artist": "B.B. King",
            "title": "Let Me Make You Cry a Little Longer",
            "kids_safe": 0.99,
            "love": 0.05,
            "mood": 0.85,
            "length": 0.13,
            "complexity": 0.44
        },
        {
            "id": 829,
            "artist": "Dirty Vegas",
            "title": "Walkintothesun",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.65,
            "length": 0.18,
            "complexity": 0.24
        },
        {
            "id": 230,
            "artist": "The Chemical Brothers",
            "title": "This Is Not a Game",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.9,
            "length": 0.35,
            "complexity": 0.27
        },
        {
            "id": 517,
            "artist": "Rochelle",
            "title": "Think Twice",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.46,
            "length": 0.21,
            "complexity": 0.31
        },
        {
            "id": 335,
            "artist": "Alabama",
            "title": "Take a Little Trip",
            "kids_safe": 0.29,
            "love": 0.03,
            "mood": 0.985,
            "length": 0.24,
            "complexity": 0.25
        },
        {
            "id": 257,
            "artist": "The Supremes",
            "title": "This is the Story",
            "kids_safe": 0.29,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.21,
            "complexity": 0.34
        },
        {
            "id": 310,
            "artist": "O Mega",
            "title": "I Believe",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.965,
            "length": 0.34,
            "complexity": 0.16
        },
        {
            "id": 404,
            "artist": "Earth, Wind & Fire",
            "title": "Jingle Bell Rock",
            "kids_safe": 0.96,
            "love": 0.05,
            "mood": 0.87,
            "length": 0.11,
            "complexity": 0.41
        },
        {
            "id": 391,
            "artist": "Rammstein",
            "title": "Mann Gegen Mann",
            "kids_safe": 0.14,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.22,
            "complexity": 0.49
        },
        {
            "id": 315,
            "artist": "Jayo Felony",
            "title": "One Shot Kill",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.0,
            "length": 0.58,
            "complexity": 0.43
        },
        {
            "id": 118,
            "artist": "Lindsay Lohan",
            "title": "A Little More Personal",
            "kids_safe": 0.86,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.36,
            "complexity": 0.25
        },
        {
            "id": 305,
            "artist": "The Standells",
            "title": "Try It",
            "kids_safe": 0.08,
            "love": 0.15,
            "mood": 0.985,
            "length": 0.18,
            "complexity": 0.43
        },
        {
            "id": 570,
            "artist": "Loverboy",
            "title": "Turn Me Loose",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.015,
            "length": 0.27,
            "complexity": 0.18
        },
        {
            "id": 736,
            "artist": "Vic Chesnutt",
            "title": "Everything I Say",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.61,
            "length": 0.09,
            "complexity": 0.44
        },
        {
            "id": 922,
            "artist": "Jeffrey Hattrick",
            "title": "All the Way",
            "kids_safe": 0.99,
            "love": 0.23,
            "mood": 0.99,
            "length": 0.12,
            "complexity": 0.39
        },
        {
            "id": 821,
            "artist": "Patsy Cline",
            "title": "I'm Moving Along",
            "kids_safe": 0.99,
            "love": 0.2,
            "mood": 0.995,
            "length": 0.18,
            "complexity": 0.28
        },
        {
            "id": 65,
            "artist": "James Brown",
            "title": "I Got the Feeling",
            "kids_safe": 0.91,
            "love": 0.0,
            "mood": 0.78,
            "length": 0.16,
            "complexity": 0.32
        },
        {
            "id": 89,
            "artist": "Shiloh",
            "title": "Alright",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.18,
            "complexity": 0.45
        },
        {
            "id": 28,
            "artist": "Blutengel",
            "title": "Dancing in the Light",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.605,
            "length": 0.31,
            "complexity": 0.21
        },
        {
            "id": 604,
            "artist": "Volcano Choir",
            "title": "Byegone",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.15,
            "length": 0.19,
            "complexity": 0.53
        },
        {
            "id": 222,
            "artist": "Erasure",
            "title": "All This Time Still Falling out of Love [Album Version]",
            "kids_safe": 1.0,
            "love": 0.3,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.27
        },
        {
            "id": 41,
            "artist": "The Chemical Brothers",
            "title": "The Salmon Dance",
            "kids_safe": 0.0,
            "love": 0.04,
            "mood": 0.99,
            "length": 0.4,
            "complexity": 0.42
        },
        {
            "id": 770,
            "artist": "Steven Maglio",
            "title": "Drinking Again",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.87,
            "length": 0.2,
            "complexity": 0.4
        },
        {
            "id": 172,
            "artist": "Jordan Smith",
            "title": "Halo",
            "kids_safe": 1.0,
            "love": 0.02,
            "mood": 0.98,
            "length": 0.29,
            "complexity": 0.29
        },
        {
            "id": 527,
            "artist": "Johnny Rivers",
            "title": "Days of Wine and Roses",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.91,
            "length": 0.09,
            "complexity": 0.36
        },
        {
            "id": 531,
            "artist": "Billy Miles",
            "title": "Sunshine",
            "kids_safe": 0.79,
            "love": 0.06,
            "mood": 0.98,
            "length": 0.38,
            "complexity": 0.36
        },
        {
            "id": 108,
            "artist": "Santo & Johnny",
            "title": "Deep Purple",
            "kids_safe": 0.87,
            "love": 0.17,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.24
        },
        {
            "id": 833,
            "artist": "Vanessa Paradis",
            "title": "Divine Idylle",
            "kids_safe": 0.87,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.12,
            "complexity": 0.57
        },
        {
            "id": 666,
            "artist": "Ariel Ram\u00edrez",
            "title": "Alfonsina y el Mar",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.065,
            "length": 0.23,
            "complexity": 0.51
        },
        {
            "id": 426,
            "artist": "Rex Foster",
            "title": "Song to Woody",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.68,
            "length": 0.19,
            "complexity": 0.45
        },
        {
            "id": 211,
            "artist": "Moony",
            "title": "Flying Away [At Mendoza vs. Tibet Club Mix]",
            "kids_safe": 0.41,
            "love": 0.09,
            "mood": 0.77,
            "length": 0.12,
            "complexity": 0.39
        },
        {
            "id": 590,
            "artist": "Juliane Werding",
            "title": "Nacht Voll Schatten",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.31,
            "complexity": 0.31
        },
        {
            "id": 783,
            "artist": "Rex Foster",
            "title": "Song to Woody",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.68,
            "length": 0.19,
            "complexity": 0.45
        },
        {
            "id": 642,
            "artist": "The Orchestra",
            "title": "Overture (LP version) [*]",
            "kids_safe": 0.99,
            "love": 0.03,
            "mood": 0.98,
            "length": 0.24,
            "complexity": 0.44
        },
        {
            "id": 290,
            "artist": "Ghost Town Blues Band",
            "title": "Come Together",
            "kids_safe": 0.15,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.19,
            "complexity": 0.37
        },
        {
            "id": 462,
            "artist": "Riot",
            "title": "Hard Lovin' Man",
            "kids_safe": 0.73,
            "love": 0.04,
            "mood": 0.925,
            "length": 0.13,
            "complexity": 0.37
        },
        {
            "id": 904,
            "artist": "Das EFX",
            "title": "Baknaffek",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.835,
            "length": 0.6,
            "complexity": 0.47
        },
        {
            "id": 969,
            "artist": "Ice Cube",
            "title": "Sasquatch",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.53,
            "complexity": 0.36
        },
        {
            "id": 997,
            "artist": "Mario Lanza",
            "title": "Funicul\u00ec, Funicul\u00e0",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 0.995,
            "length": 0.22,
            "complexity": 0.43
        },
        {
            "id": 390,
            "artist": "Love",
            "title": "My Little Red Book",
            "kids_safe": 0.97,
            "love": 0.05,
            "mood": 0.115,
            "length": 0.16,
            "complexity": 0.4
        },
        {
            "id": 355,
            "artist": "Todd and Susan Green",
            "title": "Were It Not for Grace",
            "kids_safe": 0.99,
            "love": 0.09,
            "mood": 0.885,
            "length": 0.17,
            "complexity": 0.43
        },
        {
            "id": 536,
            "artist": "Belo",
            "title": "Amante, Amor, Amiga",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.84,
            "length": 0.11,
            "complexity": 0.73
        },
        {
            "id": 429,
            "artist": "They Might Be Giants",
            "title": "Hall of Heads",
            "kids_safe": 0.79,
            "love": 0.0,
            "mood": 0.83,
            "length": 0.09,
            "complexity": 0.4
        },
        {
            "id": 917,
            "artist": "Fergie",
            "title": "Big Girls Don't Cry",
            "kids_safe": 0.11,
            "love": 0.02,
            "mood": 1.0,
            "length": 0.38,
            "complexity": 0.25
        },
        {
            "id": 912,
            "artist": "Memphis Slim",
            "title": "Caught the Old Coon at Last",
            "kids_safe": 0.09,
            "love": 0.35,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.29
        },
        {
            "id": 454,
            "artist": "Piero Odorici",
            "title": "Over the Rainbow",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.98,
            "length": 0.21,
            "complexity": 0.25
        },
        {
            "id": 910,
            "artist": "The Belmonts",
            "title": "A Teenager in Love",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.24,
            "complexity": 0.21
        },
        {
            "id": 156,
            "artist": "The Dimes",
            "title": "Anyday",
            "kids_safe": 0.97,
            "love": 0.04,
            "mood": 0.96,
            "length": 0.18,
            "complexity": 0.42
        },
        {
            "id": 816,
            "artist": "Michelle Williams",
            "title": "Heard a Word",
            "kids_safe": 0.77,
            "love": 0.03,
            "mood": 1.0,
            "length": 0.43,
            "complexity": 0.35
        },
        {
            "id": 742,
            "artist": "The Mary Jane Girls",
            "title": "All Night Long",
            "kids_safe": 0.86,
            "love": 0.11,
            "mood": 1.0,
            "length": 0.5,
            "complexity": 0.19
        },
        {
            "id": 474,
            "artist": "Marvin Gaye",
            "title": "Third World Girl",
            "kids_safe": 0.96,
            "love": 0.25,
            "mood": 0.99,
            "length": 0.12,
            "complexity": 0.45
        },
        {
            "id": 83,
            "artist": "Larry Gillespie",
            "title": "You'd Be So Nice to Come Home To",
            "kids_safe": 0.86,
            "love": 0.35,
            "mood": 0.995,
            "length": 0.08,
            "complexity": 0.29
        },
        {
            "id": 689,
            "artist": "Fairport Convention",
            "title": "Reynard the Fox",
            "kids_safe": 0.3,
            "love": 0.0,
            "mood": 0.785,
            "length": 0.18,
            "complexity": 0.46
        },
        {
            "id": 192,
            "artist": "Tex Beneke",
            "title": "These Foolish Things",
            "kids_safe": 1.0,
            "love": 0.18,
            "mood": 0.91,
            "length": 0.38,
            "complexity": 0.36
        },
        {
            "id": 499,
            "artist": "The Yardbirds",
            "title": "Shapes of Things",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.895,
            "length": 0.11,
            "complexity": 0.53
        },
        {
            "id": 986,
            "artist": "Joe Arroyo Y La Verdad",
            "title": "Pa'l Bailador",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.045,
            "length": 0.34,
            "complexity": 0.18
        },
        {
            "id": 352,
            "artist": "Buy This Song",
            "title": "Ha Ha Said the Clown",
            "kids_safe": 0.48,
            "love": 0.04,
            "mood": 0.885,
            "length": 0.17,
            "complexity": 0.55
        },
        {
            "id": 414,
            "artist": "Jefferson Airplane",
            "title": "Come Back Baby",
            "kids_safe": 0.81,
            "love": 0.0,
            "mood": 0.66,
            "length": 0.05,
            "complexity": 0.29
        },
        {
            "id": 48,
            "artist": "Perry Como",
            "title": "Silent Night",
            "kids_safe": 0.76,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.1,
            "complexity": 0.57
        },
        {
            "id": 972,
            "artist": "Big Bill Broonzy",
            "title": "Baby I Done Got Wise",
            "kids_safe": 0.72,
            "love": 0.03,
            "mood": 0.99,
            "length": 0.27,
            "complexity": 0.25
        },
        {
            "id": 298,
            "artist": "Keith Caputo",
            "title": "Just Be",
            "kids_safe": 0.93,
            "love": 0.16,
            "mood": 0.215,
            "length": 0.08,
            "complexity": 0.6
        },
        {
            "id": 247,
            "artist": "John Fahey",
            "title": "Blueberry Hill",
            "kids_safe": 0.94,
            "love": 0.12,
            "mood": 0.98,
            "length": 0.1,
            "complexity": 0.31
        },
        {
            "id": 629,
            "artist": "The Beatles",
            "title": "From Me to You",
            "kids_safe": 0.01,
            "love": 0.1,
            "mood": 0.99,
            "length": 0.21,
            "complexity": 0.14
        },
        {
            "id": 154,
            "artist": "Mango",
            "title": "Mediterraneo",
            "kids_safe": 0.8,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.16,
            "complexity": 0.59
        },
        {
            "id": 184,
            "artist": "Beth Orton",
            "title": "Best Bit",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.87,
            "length": 0.14,
            "complexity": 0.36
        },
        {
            "id": 197,
            "artist": "Slam Stewart",
            "title": "I'm in the Mood for Love",
            "kids_safe": 0.69,
            "love": 0.15,
            "mood": 0.995,
            "length": 0.09,
            "complexity": 0.45
        },
        {
            "id": 786,
            "artist": "Gomez",
            "title": "78 Stone Wobble",
            "kids_safe": 0.02,
            "love": 0.0,
            "mood": 0.015,
            "length": 0.19,
            "complexity": 0.15
        },
        {
            "id": 503,
            "artist": "Ted Taylor",
            "title": "It's Too Late",
            "kids_safe": 0.06,
            "love": 0.06,
            "mood": 0.045,
            "length": 0.23,
            "complexity": 0.31
        },
        {
            "id": 461,
            "artist": "Todd Isler",
            "title": "Too High",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.86,
            "length": 0.27,
            "complexity": 0.27
        },
        {
            "id": 699,
            "artist": "Carmen McRae",
            "title": "Just One of Those Things",
            "kids_safe": 1.0,
            "love": 0.16,
            "mood": 0.995,
            "length": 0.23,
            "complexity": 0.31
        },
        {
            "id": 735,
            "artist": "Johnny Cash",
            "title": "I Walk the Line",
            "kids_safe": 0.92,
            "love": 0.17,
            "mood": 0.975,
            "length": 0.18,
            "complexity": 0.3
        },
        {
            "id": 584,
            "artist": "Marian McPartland",
            "title": "Once in a While",
            "kids_safe": 0.99,
            "love": 0.11,
            "mood": 0.985,
            "length": 0.12,
            "complexity": 0.34
        },
        {
            "id": 526,
            "artist": "The Lemonheads",
            "title": "Alison's Starting to Happen",
            "kids_safe": 0.14,
            "love": 0.0,
            "mood": 0.115,
            "length": 0.17,
            "complexity": 0.43
        },
        {
            "id": 209,
            "artist": "Jos\u00e9 Feliciano",
            "title": "Ahora Si Quiero Amar",
            "kids_safe": 0.57,
            "love": 0.06,
            "mood": 0.99,
            "length": 0.25,
            "complexity": 0.27
        },
        {
            "id": 313,
            "artist": "Bouzouki Ensemble",
            "title": "Never On Sunday",
            "kids_safe": 0.05,
            "love": 0.24,
            "mood": 0.985,
            "length": 0.17,
            "complexity": 0.3
        },
        {
            "id": 260,
            "artist": "Ra Ra Riot",
            "title": "Binary Mind",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.29,
            "complexity": 0.25
        },
        {
            "id": 415,
            "artist": "Refused",
            "title": "Burn It",
            "kids_safe": 0.01,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.25,
            "complexity": 0.34
        },
        {
            "id": 998,
            "artist": "Esperanza Spalding",
            "title": "Funk the Fear",
            "kids_safe": 0.01,
            "love": 0.0,
            "mood": 0.115,
            "length": 0.46,
            "complexity": 0.26
        },
        {
            "id": 903,
            "artist": "Louis Armstrong",
            "title": "Makin' Whoopee",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 0.98,
            "length": 0.2,
            "complexity": 0.55
        },
        {
            "id": 271,
            "artist": "E 40",
            "title": "Neva Broke",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.02,
            "length": 0.77,
            "complexity": 0.42
        },
        {
            "id": 348,
            "artist": "Luis\u00e3o",
            "title": "Romaria",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.21,
            "complexity": 0.38
        },
        {
            "id": 563,
            "artist": "Goo Goo Dolls",
            "title": "Iris [Album Version]",
            "kids_safe": 0.98,
            "love": 0.04,
            "mood": 0.215,
            "length": 0.25,
            "complexity": 0.19
        },
        {
            "id": 58,
            "artist": "Crimson Glory",
            "title": "In the Mood",
            "kids_safe": 0.87,
            "love": 0.3,
            "mood": 0.975,
            "length": 0.28,
            "complexity": 0.35
        },
        {
            "id": 947,
            "artist": "Sam Cooke",
            "title": "Trouble Blues",
            "kids_safe": 0.93,
            "love": 0.27,
            "mood": 0.98,
            "length": 0.08,
            "complexity": 0.37
        },
        {
            "id": 91,
            "artist": "Ash",
            "title": "Envy",
            "kids_safe": 0.86,
            "love": 0.05,
            "mood": 0.005,
            "length": 0.24,
            "complexity": 0.47
        },
        {
            "id": 868,
            "artist": "Grin",
            "title": "White Lies",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.2,
            "complexity": 0.31
        },
        {
            "id": 69,
            "artist": "Asia",
            "title": "Don't Cry [Live]",
            "kids_safe": 0.93,
            "love": 0.06,
            "mood": 0.97,
            "length": 0.12,
            "complexity": 0.4
        },
        {
            "id": 869,
            "artist": "Big L",
            "title": "Put It On",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.015,
            "length": 0.75,
            "complexity": 0.37
        },
        {
            "id": 385,
            "artist": "Natalia Oreiro",
            "title": "Sabrosito Y Dulz\u00f3n",
            "kids_safe": 0.49,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.11,
            "complexity": 0.57
        },
        {
            "id": 208,
            "artist": "Buzzcocks",
            "title": "Jerk",
            "kids_safe": 0.94,
            "love": 0.18,
            "mood": 0.995,
            "length": 0.24,
            "complexity": 0.21
        },
        {
            "id": 515,
            "artist": "Domenico Modugno",
            "title": "La Lontananza",
            "kids_safe": 0.53,
            "love": 0.0,
            "mood": 0.05,
            "length": 0.27,
            "complexity": 0.54
        },
        {
            "id": 76,
            "artist": "John Basile",
            "title": "That Old Feeling",
            "kids_safe": 0.99,
            "love": 0.36,
            "mood": 0.99,
            "length": 0.21,
            "complexity": 0.26
        },
        {
            "id": 79,
            "artist": "Shalamar",
            "title": "Take That to the Bank",
            "kids_safe": 1.0,
            "love": 0.42,
            "mood": 1.0,
            "length": 0.33,
            "complexity": 0.28
        },
        {
            "id": 73,
            "artist": "Down",
            "title": "Levitation",
            "kids_safe": 0.34,
            "love": 0.0,
            "mood": 0.2,
            "length": 0.11,
            "complexity": 0.58
        },
        {
            "id": 361,
            "artist": "Dolly Parton",
            "title": "Puppy Love",
            "kids_safe": 0.03,
            "love": 0.64,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.29
        },
        {
            "id": 264,
            "artist": "Jimmy Beasley",
            "title": "Coquette",
            "kids_safe": 0.64,
            "love": 0.66,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.26
        },
        {
            "id": 430,
            "artist": "Jason Isbell and the 400 Unit",
            "title": "Dress Blues",
            "kids_safe": 1.0,
            "love": 0.1,
            "mood": 0.84,
            "length": 0.28,
            "complexity": 0.42
        },
        {
            "id": 182,
            "artist": "Cream",
            "title": "Born Under a Bad Sign",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.13,
            "complexity": 0.22
        },
        {
            "id": 374,
            "artist": "Jimmy Dorsey & His Orchestra",
            "title": "Begin the Beguine",
            "kids_safe": 0.99,
            "love": 0.18,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.38
        },
        {
            "id": 465,
            "artist": "An\u00edbal Troilo",
            "title": "Sur",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.82,
            "length": 0.18,
            "complexity": 0.6
        },
        {
            "id": 755,
            "artist": "David",
            "title": "Nature Boy",
            "kids_safe": 0.95,
            "love": 0.24,
            "mood": 0.98,
            "length": 0.09,
            "complexity": 0.52
        },
        {
            "id": 103,
            "artist": "Take That",
            "title": "The Garden",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.99,
            "length": 0.28,
            "complexity": 0.32
        },
        {
            "id": 793,
            "artist": "Leslie Phillips",
            "title": "River of Love",
            "kids_safe": 1.0,
            "love": 0.35,
            "mood": 0.79,
            "length": 0.21,
            "complexity": 0.32
        },
        {
            "id": 443,
            "artist": "Jimmy Giuffre",
            "title": "Deep Purple",
            "kids_safe": 0.87,
            "love": 0.17,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.24
        },
        {
            "id": 644,
            "artist": "Christopher Boscole",
            "title": "O Little Town of Bethlehem",
            "kids_safe": 0.63,
            "love": 0.09,
            "mood": 0.96,
            "length": 0.13,
            "complexity": 0.39
        },
        {
            "id": 114,
            "artist": "Starsailor",
            "title": "Listen Up",
            "kids_safe": 0.46,
            "love": 0.0,
            "mood": 0.29,
            "length": 0.13,
            "complexity": 0.28
        },
        {
            "id": 61,
            "artist": "Terence Trent D'Arby",
            "title": "If You All Get to Heaven",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.38,
            "complexity": 0.33
        },
        {
            "id": 964,
            "artist": "Cornelio Reyna",
            "title": "Te Vas Angel Mio",
            "kids_safe": 0.94,
            "love": 0.0,
            "mood": 0.73,
            "length": 0.1,
            "complexity": 0.48
        },
        {
            "id": 653,
            "artist": "Sigur R\u00f3s",
            "title": "Svefn G Englar",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.1,
            "complexity": 0.69
        },
        {
            "id": 880,
            "artist": "Ludacris",
            "title": "Gossip Folks",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.0,
            "length": 0.78,
            "complexity": 0.43
        },
        {
            "id": 413,
            "artist": "Jenny Evans",
            "title": "Old Devil Moon [From Finian's Rainbow]",
            "kids_safe": 0.41,
            "love": 0.11,
            "mood": 0.205,
            "length": 0.12,
            "complexity": 0.51
        },
        {
            "id": 801,
            "artist": "Barbara & Al Boudreau",
            "title": "I'm Old Fashioned",
            "kids_safe": 0.98,
            "love": 0.13,
            "mood": 0.96,
            "length": 0.15,
            "complexity": 0.37
        },
        {
            "id": 519,
            "artist": "Chris Botti",
            "title": "Lola's Mambo",
            "kids_safe": 0.89,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.4,
            "complexity": 0.22
        },
        {
            "id": 846,
            "artist": "Wes Montgomery",
            "title": "On Green Dolphin Street [Take 2]",
            "kids_safe": 1.0,
            "love": 0.24,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.37
        },
        {
            "id": 84,
            "artist": "Andy Timmons",
            "title": "Slips Away [*]",
            "kids_safe": 0.63,
            "love": 0.09,
            "mood": 0.16,
            "length": 0.15,
            "complexity": 0.35
        },
        {
            "id": 949,
            "artist": "John Skinner",
            "title": "Tequila",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.5,
            "complexity": 0.45
        },
        {
            "id": 5,
            "artist": "Ronan Keating",
            "title": "Time After Time",
            "kids_safe": 0.81,
            "love": 0.0,
            "mood": 0.085,
            "length": 0.21,
            "complexity": 0.31
        },
        {
            "id": 252,
            "artist": "Renaud",
            "title": "Rita (Chanson d'Amour)",
            "kids_safe": 0.83,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.02,
            "complexity": 0.61
        },
        {
            "id": 988,
            "artist": "Whiskeytown",
            "title": "What the Devil Wanted",
            "kids_safe": 0.42,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.14,
            "complexity": 0.25
        },
        {
            "id": 730,
            "artist": "Buy This Song",
            "title": "Sophisticated Lady",
            "kids_safe": 0.53,
            "love": 0.06,
            "mood": 1.0,
            "length": 0.2,
            "complexity": 0.3
        },
        {
            "id": 275,
            "artist": "Terrel, Tammi",
            "title": "You're All I Need to Get By",
            "kids_safe": 0.97,
            "love": 0.12,
            "mood": 0.995,
            "length": 0.21,
            "complexity": 0.43
        },
        {
            "id": 987,
            "artist": "Thurston Moore",
            "title": "Female Cop",
            "kids_safe": 0.68,
            "love": 0.17,
            "mood": 0.565,
            "length": 0.12,
            "complexity": 0.22
        },
        {
            "id": 446,
            "artist": "Terry Callier",
            "title": "Ordinary Joe",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.62,
            "length": 0.37,
            "complexity": 0.37
        },
        {
            "id": 359,
            "artist": "Bobby Solo",
            "title": "Una Lacrima Sul Viso",
            "kids_safe": 0.32,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.09,
            "complexity": 0.64
        },
        {
            "id": 707,
            "artist": "Frank Griffith",
            "title": "Body and Soul",
            "kids_safe": 0.86,
            "love": 0.23,
            "mood": 0.86,
            "length": 0.14,
            "complexity": 0.35
        },
        {
            "id": 981,
            "artist": "The Everly Brothers",
            "title": "Bye Bye Love",
            "kids_safe": 0.57,
            "love": 0.43,
            "mood": 1.0,
            "length": 0.19,
            "complexity": 0.24
        },
        {
            "id": 580,
            "artist": "Dir en Grey",
            "title": "Merciless Cult",
            "kids_safe": 0.01,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.06,
            "complexity": 0.35
        },
        {
            "id": 31,
            "artist": "The Statler Brothers",
            "title": "Just a Little Talk with Jesus",
            "kids_safe": 0.83,
            "love": 0.08,
            "mood": 0.015,
            "length": 0.27,
            "complexity": 0.21
        },
        {
            "id": 311,
            "artist": "Blue Mink",
            "title": "Good Morning Freedom",
            "kids_safe": 0.06,
            "love": 0.03,
            "mood": 0.995,
            "length": 0.22,
            "complexity": 0.36
        },
        {
            "id": 441,
            "artist": "Eddy Arnold",
            "title": "A Heart Full of Love",
            "kids_safe": 1.0,
            "love": 0.72,
            "mood": 0.99,
            "length": 0.17,
            "complexity": 0.31
        },
        {
            "id": 655,
            "artist": "Dave Costa",
            "title": "Serenade in Blue",
            "kids_safe": 1.0,
            "love": 0.11,
            "mood": 0.895,
            "length": 0.12,
            "complexity": 0.51
        },
        {
            "id": 765,
            "artist": "Scott Walker",
            "title": "Psoriatic",
            "kids_safe": 0.44,
            "love": 0.02,
            "mood": 0.045,
            "length": 0.28,
            "complexity": 0.31
        },
        {
            "id": 289,
            "artist": "Patricia Neway",
            "title": "Climb Ev'ry Mountain",
            "kids_safe": 0.99,
            "love": 0.11,
            "mood": 0.97,
            "length": 0.1,
            "complexity": 0.24
        },
        {
            "id": 318,
            "artist": "Trick Pony",
            "title": "Pour Me",
            "kids_safe": 0.14,
            "love": 0.1,
            "mood": 0.01,
            "length": 0.28,
            "complexity": 0.25
        },
        {
            "id": 248,
            "artist": "Nate James",
            "title": "Pretend",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.955,
            "length": 0.37,
            "complexity": 0.27
        },
        {
            "id": 419,
            "artist": "Michael Ross",
            "title": "That Summer Night",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.99,
            "length": 0.22,
            "complexity": 0.32
        },
        {
            "id": 481,
            "artist": "Angelcorpse",
            "title": "The Scapegoat",
            "kids_safe": 0.85,
            "love": 0.0,
            "mood": 0.065,
            "length": 0.15,
            "complexity": 0.52
        },
        {
            "id": 769,
            "artist": "Billy Vaughn",
            "title": "I Left My Heart in San Francisco",
            "kids_safe": 1.0,
            "love": 0.22,
            "mood": 0.04,
            "length": 0.12,
            "complexity": 0.27
        },
        {
            "id": 284,
            "artist": "Rick Wakeman",
            "title": "Eleanor Rigby",
            "kids_safe": 0.98,
            "love": 0.04,
            "mood": 0.01,
            "length": 0.2,
            "complexity": 0.3
        },
        {
            "id": 303,
            "artist": "Bing Crosby",
            "title": "I Surrender Dear [#]",
            "kids_safe": 0.75,
            "love": 0.22,
            "mood": 0.91,
            "length": 0.25,
            "complexity": 0.29
        },
        {
            "id": 525,
            "artist": "Rappin' 4 Tay",
            "title": "Sweet Love",
            "kids_safe": 0.0,
            "love": 0.11,
            "mood": 0.03,
            "length": 0.77,
            "complexity": 0.44
        },
        {
            "id": 578,
            "artist": "Mano Negra",
            "title": "King Kong Five",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.43,
            "complexity": 0.13
        },
        {
            "id": 874,
            "artist": "Asia",
            "title": "Time Again",
            "kids_safe": 0.99,
            "love": 0.05,
            "mood": 0.115,
            "length": 0.15,
            "complexity": 0.38
        },
        {
            "id": 573,
            "artist": "Matteo Brancaleoni",
            "title": "Copacabana",
            "kids_safe": 0.69,
            "love": 0.15,
            "mood": 0.945,
            "length": 0.25,
            "complexity": 0.39
        },
        {
            "id": 447,
            "artist": "Carina Round",
            "title": "Ready to Confess",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.31
        },
        {
            "id": 259,
            "artist": "David Bowie",
            "title": "Cracked Actor",
            "kids_safe": 0.0,
            "love": 0.04,
            "mood": 0.12,
            "length": 0.17,
            "complexity": 0.42
        },
        {
            "id": 395,
            "artist": "NOFX",
            "title": "Lori Meyers",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.17,
            "complexity": 0.52
        },
        {
            "id": 488,
            "artist": "ABBA",
            "title": "Mamma Mia",
            "kids_safe": 1.0,
            "love": 0.02,
            "mood": 0.005,
            "length": 0.33,
            "complexity": 0.24
        },
        {
            "id": 759,
            "artist": "Tiktak",
            "title": "Tuuleksi Taivaanrantaan",
            "kids_safe": 0.61,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.18,
            "complexity": 0.54
        },
        {
            "id": 485,
            "artist": "John Mellencamp",
            "title": "This May Not Be the End of the World",
            "kids_safe": 0.98,
            "love": 0.03,
            "mood": 0.965,
            "length": 0.3,
            "complexity": 0.33
        },
        {
            "id": 720,
            "artist": "Terrorvision",
            "title": "Tequila (Mint Royale Shot)",
            "kids_safe": 0.8,
            "love": 0.04,
            "mood": 0.035,
            "length": 0.16,
            "complexity": 0.41
        },
        {
            "id": 265,
            "artist": "Fats Waller",
            "title": "I'm Crazy 'Bout My Baby",
            "kids_safe": 0.49,
            "love": 0.06,
            "mood": 0.935,
            "length": 0.11,
            "complexity": 0.43
        },
        {
            "id": 216,
            "artist": "Lee Greenwood",
            "title": "I.O.U.",
            "kids_safe": 0.49,
            "love": 0.0,
            "mood": 0.935,
            "length": 0.22,
            "complexity": 0.28
        },
        {
            "id": 369,
            "artist": "Tee",
            "title": "Think Twice",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.46,
            "length": 0.21,
            "complexity": 0.31
        },
        {
            "id": 979,
            "artist": "Atrocity",
            "title": "Die Liebe",
            "kids_safe": 0.14,
            "love": 0.0,
            "mood": 0.045,
            "length": 0.01,
            "complexity": 0.89
        },
        {
            "id": 814,
            "artist": "John Renbourn",
            "title": "Lord Franklin",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.08,
            "length": 0.16,
            "complexity": 0.56
        },
        {
            "id": 995,
            "artist": "Willie Bobo",
            "title": "Knock on Wood",
            "kids_safe": 1.0,
            "love": 0.25,
            "mood": 1.0,
            "length": 0.25,
            "complexity": 0.25
        },
        {
            "id": 762,
            "artist": "Reba McEntire",
            "title": "Santa Claus Is Coming to Town",
            "kids_safe": 0.87,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.36,
            "complexity": 0.31
        },
        {
            "id": 513,
            "artist": "Dalida",
            "title": "Bambino",
            "kids_safe": 0.42,
            "love": 0.0,
            "mood": 0.13,
            "length": 0.31,
            "complexity": 0.51
        },
        {
            "id": 591,
            "artist": "The Notorious B.I.G.",
            "title": "The Commission",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.005,
            "length": 0.53,
            "complexity": 0.54
        },
        {
            "id": 169,
            "artist": "The Band Perry",
            "title": "Uptown Funk",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.995,
            "length": 0.66,
            "complexity": 0.18
        },
        {
            "id": 375,
            "artist": "Bob Marley",
            "title": "Corner Stone",
            "kids_safe": 0.15,
            "love": 0.0,
            "mood": 0.015,
            "length": 0.19,
            "complexity": 0.2
        },
        {
            "id": 333,
            "artist": "Johnny Burnette",
            "title": "You're Sixteen",
            "kids_safe": 0.75,
            "love": 0.3,
            "mood": 1.0,
            "length": 0.18,
            "complexity": 0.26
        },
        {
            "id": 992,
            "artist": "Miles Davis",
            "title": "I Fall in Love Too Easily (A)",
            "kids_safe": 0.99,
            "love": 0.97,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.15
        },
        {
            "id": 343,
            "artist": "Yes",
            "title": "Yours Is No Disgrace",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.23,
            "complexity": 0.23
        },
        {
            "id": 785,
            "artist": "Mark Morrison",
            "title": "Crazy [Album Version]",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.87,
            "length": 0.37,
            "complexity": 0.41
        },
        {
            "id": 521,
            "artist": "145th Street",
            "title": "Mary Ann",
            "kids_safe": 1.0,
            "love": 0.24,
            "mood": 0.995,
            "length": 0.16,
            "complexity": 0.33
        },
        {
            "id": 630,
            "artist": "Cherise",
            "title": "Other Half",
            "kids_safe": 0.97,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.41,
            "complexity": 0.22
        },
        {
            "id": 809,
            "artist": "Buy This Song",
            "title": "I Wonder",
            "kids_safe": 0.97,
            "love": 0.36,
            "mood": 0.985,
            "length": 0.12,
            "complexity": 0.38
        },
        {
            "id": 712,
            "artist": "Ike Quebec",
            "title": "It Might As Well Be Spring",
            "kids_safe": 0.51,
            "love": 0.0,
            "mood": 0.205,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 448,
            "artist": "Shirley Bassey",
            "title": "Goldfinger",
            "kids_safe": 0.7,
            "love": 0.54,
            "mood": 0.825,
            "length": 0.14,
            "complexity": 0.29
        },
        {
            "id": 600,
            "artist": "Topi Sorsakoski",
            "title": "Mona Lisa",
            "kids_safe": 0.83,
            "love": 0.0,
            "mood": 0.945,
            "length": 0.15,
            "complexity": 0.27
        },
        {
            "id": 990,
            "artist": "Tommy Steele",
            "title": "A Handful of Songs",
            "kids_safe": 0.98,
            "love": 0.19,
            "mood": 0.96,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 6,
            "artist": "The Pussycat Dolls",
            "title": "Hush Hush; Hush Hush [Main]",
            "kids_safe": 0.97,
            "love": 0.1,
            "mood": 0.855,
            "length": 0.24,
            "complexity": 0.34
        },
        {
            "id": 725,
            "artist": "The Mavericks",
            "title": "La Mucara [#]",
            "kids_safe": 0.22,
            "love": 0.0,
            "mood": 0.91,
            "length": 0.29,
            "complexity": 0.23
        },
        {
            "id": 358,
            "artist": "Back Door Slam",
            "title": "Outside Woman Blues",
            "kids_safe": 0.06,
            "love": 0.31,
            "mood": 0.655,
            "length": 0.17,
            "complexity": 0.3
        },
        {
            "id": 47,
            "artist": "Brezz Zelenka",
            "title": "Tupelo Honey",
            "kids_safe": 1.0,
            "love": 0.39,
            "mood": 0.995,
            "length": 0.21,
            "complexity": 0.31
        },
        {
            "id": 148,
            "artist": "Z.Z. Hill",
            "title": "Put a Little Love in Your Heart [*]",
            "kids_safe": 0.94,
            "love": 0.62,
            "mood": 1.0,
            "length": 0.2,
            "complexity": 0.21
        },
        {
            "id": 64,
            "artist": "Emerson, Lake & Palmer",
            "title": "Lucky Man",
            "kids_safe": 0.31,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.14,
            "complexity": 0.35
        },
        {
            "id": 138,
            "artist": "Tommy Steele",
            "title": "A Handful of Songs",
            "kids_safe": 0.98,
            "love": 0.19,
            "mood": 0.96,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 440,
            "artist": "John Williamson",
            "title": "Dingo",
            "kids_safe": 0.1,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.08,
            "complexity": 0.24
        },
        {
            "id": 227,
            "artist": "John Mayer",
            "title": "Edge of Desire",
            "kids_safe": 0.99,
            "love": 0.03,
            "mood": 0.015,
            "length": 0.25,
            "complexity": 0.29
        },
        {
            "id": 171,
            "artist": "Kirk Whalum",
            "title": "Any Love",
            "kids_safe": 0.84,
            "love": 0.37,
            "mood": 1.0,
            "length": 0.28,
            "complexity": 0.32
        },
        {
            "id": 624,
            "artist": "Grupo Mont\u00e9z de Durango",
            "title": "Jambalaya",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 832,
            "artist": "Tokio Hotel",
            "title": "Reden",
            "kids_safe": 0.65,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.19,
            "complexity": 0.59
        },
        {
            "id": 416,
            "artist": "Blanca",
            "title": "Chosen Ones",
            "kids_safe": 0.71,
            "love": 0.41,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.22
        },
        {
            "id": 627,
            "artist": "Coleman Hawkins",
            "title": "Day by Day",
            "kids_safe": 0.83,
            "love": 0.49,
            "mood": 0.985,
            "length": 0.08,
            "complexity": 0.39
        },
        {
            "id": 137,
            "artist": "Beyonc\u00e9",
            "title": "Ego [Fan Exclusive] [Video]",
            "kids_safe": 0.1,
            "love": 0.06,
            "mood": 1.0,
            "length": 0.47,
            "complexity": 0.25
        },
        {
            "id": 710,
            "artist": "Blues Alliance",
            "title": "Isn't That So",
            "kids_safe": 1.0,
            "love": 0.2,
            "mood": 0.795,
            "length": 0.22,
            "complexity": 0.23
        },
        {
            "id": 690,
            "artist": "Michael Mcleavy",
            "title": "Danny Boy",
            "kids_safe": 0.65,
            "love": 0.09,
            "mood": 0.79,
            "length": 0.16,
            "complexity": 0.44
        },
        {
            "id": 435,
            "artist": "Shirley Bassey",
            "title": "Spinning Wheel [DJ Spinna Remix]",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.11,
            "complexity": 0.47
        },
        {
            "id": 937,
            "artist": "Slaughter & the Dogs",
            "title": "Who Are the Mystery Girls?",
            "kids_safe": 0.09,
            "love": 0.08,
            "mood": 0.975,
            "length": 0.36,
            "complexity": 0.18
        },
        {
            "id": 268,
            "artist": "Imix Children's Choir",
            "title": "Paseo en Trineo (Sleigh Ride)",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 845,
            "artist": "Kiki Dee",
            "title": "Star",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.66,
            "length": 0.25,
            "complexity": 0.33
        },
        {
            "id": 668,
            "artist": "The Pointer Sisters",
            "title": "Be There",
            "kids_safe": 0.91,
            "love": 0.02,
            "mood": 0.005,
            "length": 0.37,
            "complexity": 0.23
        },
        {
            "id": 387,
            "artist": "Neil Young & Crazy Horse",
            "title": "Blowin' in the Wind",
            "kids_safe": 0.5,
            "love": 0.04,
            "mood": 0.98,
            "length": 0.19,
            "complexity": 0.27
        },
        {
            "id": 21,
            "artist": "Van Dyke Parks",
            "title": "The All Golden",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.805,
            "length": 0.18,
            "complexity": 0.46
        },
        {
            "id": 920,
            "artist": "Julio Jaramillo",
            "title": "Odiame",
            "kids_safe": 0.6,
            "love": 0.0,
            "mood": 0.1,
            "length": 0.2,
            "complexity": 0.28
        },
        {
            "id": 507,
            "artist": "Tommy Emmanuel",
            "title": "Lover Come Back to Me",
            "kids_safe": 0.69,
            "love": 0.23,
            "mood": 0.965,
            "length": 0.22,
            "complexity": 0.28
        },
        {
            "id": 555,
            "artist": "Avenged Sevenfold",
            "title": "Save Me",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.46,
            "complexity": 0.26
        },
        {
            "id": 622,
            "artist": "Jeff Bridges",
            "title": "Hold on You",
            "kids_safe": 0.99,
            "love": 0.05,
            "mood": 0.245,
            "length": 0.19,
            "complexity": 0.22
        },
        {
            "id": 738,
            "artist": "Akir",
            "title": "One",
            "kids_safe": 0.0,
            "love": 0.04,
            "mood": 1.0,
            "length": 0.69,
            "complexity": 0.45
        },
        {
            "id": 250,
            "artist": "Matt Monro",
            "title": "(They Long to Be) Close to You",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.18,
            "complexity": 0.23
        },
        {
            "id": 279,
            "artist": "Stephanie",
            "title": "It Had to Be You",
            "kids_safe": 0.96,
            "love": 0.08,
            "mood": 0.98,
            "length": 0.18,
            "complexity": 0.23
        },
        {
            "id": 714,
            "artist": "Claude Nougaro",
            "title": "Toulouse",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.35,
            "length": 0.24,
            "complexity": 0.69
        },
        {
            "id": 576,
            "artist": "Nightwish",
            "title": "Higher Than Hope",
            "kids_safe": 0.93,
            "love": 0.1,
            "mood": 0.85,
            "length": 0.13,
            "complexity": 0.53
        },
        {
            "id": 566,
            "artist": "Neil Bradley Owen",
            "title": "For What It's Worth",
            "kids_safe": 0.94,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.19,
            "complexity": 0.37
        },
        {
            "id": 296,
            "artist": "Kylie Minogue",
            "title": "Almost a Lover",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.32,
            "complexity": 0.32
        },
        {
            "id": 697,
            "artist": "Buy This Song",
            "title": "Funiculi' Funicula' [Live]",
            "kids_safe": 0.64,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.16,
            "complexity": 0.52
        },
        {
            "id": 217,
            "artist": "Michael Kwan",
            "title": "Ren Zai Lu Tu Sa Lei Shi",
            "kids_safe": 0.55,
            "love": 0.04,
            "mood": 0.79,
            "length": 0.19,
            "complexity": 0.28
        },
        {
            "id": 885,
            "artist": "Mantovani Orchestra",
            "title": "[Unspecified] Swedish Rhapsody",
            "kids_safe": 1.0,
            "love": 0.11,
            "mood": 0.86,
            "length": 0.13,
            "complexity": 0.3
        },
        {
            "id": 623,
            "artist": "Roger McGuinn",
            "title": "It Won't Be Wrong",
            "kids_safe": 1.0,
            "love": 0.53,
            "mood": 1.0,
            "length": 0.19,
            "complexity": 0.12
        },
        {
            "id": 610,
            "artist": "Alestorm",
            "title": "The Quest",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.15,
            "complexity": 0.37
        },
        {
            "id": 173,
            "artist": "Bloodhound Gang",
            "title": "It's Tricky",
            "kids_safe": 0.22,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.44,
            "complexity": 0.27
        },
        {
            "id": 718,
            "artist": "Conway Twitty",
            "title": "Red Neckin' Love Makin' Night",
            "kids_safe": 0.96,
            "love": 0.29,
            "mood": 1.0,
            "length": 0.4,
            "complexity": 0.27
        },
        {
            "id": 187,
            "artist": "Chris Hillman",
            "title": "So You Want to Be a Rock 'n' Roll Star",
            "kids_safe": 0.74,
            "love": 0.0,
            "mood": 0.925,
            "length": 0.14,
            "complexity": 0.48
        },
        {
            "id": 13,
            "artist": "You Say Party! We Say Die!",
            "title": "Monster",
            "kids_safe": 0.3,
            "love": 0.0,
            "mood": 0.55,
            "length": 0.26,
            "complexity": 0.34
        },
        {
            "id": 758,
            "artist": "Deitrick Haddon",
            "title": "Jesus Is Coming",
            "kids_safe": 0.09,
            "love": 0.09,
            "mood": 0.785,
            "length": 0.15,
            "complexity": 0.19
        },
        {
            "id": 42,
            "artist": "Elvis Presley",
            "title": "Blue Suede Shoes",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.24,
            "complexity": 0.23
        },
        {
            "id": 1000,
            "artist": "Champian Fulton",
            "title": "Easy to Love",
            "kids_safe": 0.88,
            "love": 0.36,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.48
        },
        {
            "id": 181,
            "artist": "Johnny Winter",
            "title": "Parchman Farm",
            "kids_safe": 0.07,
            "love": 0.12,
            "mood": 0.36,
            "length": 0.13,
            "complexity": 0.24
        },
        {
            "id": 779,
            "artist": "Jodeci",
            "title": "Stay",
            "kids_safe": 0.77,
            "love": 0.15,
            "mood": 0.995,
            "length": 0.31,
            "complexity": 0.29
        },
        {
            "id": 288,
            "artist": "Billie Holiday",
            "title": "No Regrets",
            "kids_safe": 0.97,
            "love": 1.0,
            "mood": 0.97,
            "length": 0.07,
            "complexity": 0.42
        },
        {
            "id": 934,
            "artist": "Jim Croce",
            "title": "You Don't Mess Around with Jim",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.955,
            "length": 0.37,
            "complexity": 0.31
        },
        {
            "id": 789,
            "artist": "Alkaline Trio",
            "title": "Hell Yes",
            "kids_safe": 0.82,
            "love": 0.1,
            "mood": 0.99,
            "length": 0.29,
            "complexity": 0.33
        },
        {
            "id": 800,
            "artist": "Eva Cassidy",
            "title": "Songbird",
            "kids_safe": 0.87,
            "love": 0.41,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.21
        },
        {
            "id": 551,
            "artist": "Carlos Gardel",
            "title": "Milonga Sentimental",
            "kids_safe": 0.52,
            "love": 0.0,
            "mood": 0.615,
            "length": 0.18,
            "complexity": 0.65
        },
        {
            "id": 849,
            "artist": "Maroon 5",
            "title": "Pure Imagination",
            "kids_safe": 0.66,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.15,
            "complexity": 0.26
        },
        {
            "id": 4,
            "artist": "Spice Girls",
            "title": "Sleigh Ride",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.18,
            "complexity": 0.27
        },
        {
            "id": 639,
            "artist": "Buy This Song",
            "title": "Superstition",
            "kids_safe": 0.91,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.21,
            "complexity": 0.28
        },
        {
            "id": 645,
            "artist": "Los \u00c1ngeles Azules",
            "title": "El  Pecado",
            "kids_safe": 0.1,
            "love": 0.0,
            "mood": 0.085,
            "length": 0.13,
            "complexity": 0.42
        },
        {
            "id": 332,
            "artist": "Me 3",
            "title": "You Don't Know What Love Is",
            "kids_safe": 0.39,
            "love": 0.61,
            "mood": 0.01,
            "length": 0.12,
            "complexity": 0.35
        },
        {
            "id": 256,
            "artist": "Am\u00e1lia Rodrigues",
            "title": "Ai Mouraria",
            "kids_safe": 0.84,
            "love": 0.0,
            "mood": 0.805,
            "length": 0.1,
            "complexity": 0.72
        },
        {
            "id": 926,
            "artist": "Oscar Peterson",
            "title": "On Green Dolphin Street",
            "kids_safe": 1.0,
            "love": 0.24,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.37
        },
        {
            "id": 340,
            "artist": "Cataract",
            "title": "Killing Tool",
            "kids_safe": 0.94,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.16,
            "complexity": 0.49
        },
        {
            "id": 853,
            "artist": "Paul Weller",
            "title": "Bring Back the Funk, Pts. 1 & 2",
            "kids_safe": 1.0,
            "love": 0.09,
            "mood": 0.99,
            "length": 0.47,
            "complexity": 0.19
        },
        {
            "id": 405,
            "artist": "Alien Sex Fiend",
            "title": "New Christian Music [DVD]",
            "kids_safe": 0.91,
            "love": 0.0,
            "mood": 0.135,
            "length": 0.11,
            "complexity": 0.42
        },
        {
            "id": 657,
            "artist": "Mother's Finest",
            "title": "Baby Love",
            "kids_safe": 0.63,
            "love": 0.34,
            "mood": 1.0,
            "length": 0.46,
            "complexity": 0.16
        },
        {
            "id": 468,
            "artist": "Lewis, John",
            "title": "I Didn't Know What Time It Was",
            "kids_safe": 1.0,
            "love": 0.12,
            "mood": 1.0,
            "length": 0.23,
            "complexity": 0.32
        },
        {
            "id": 354,
            "artist": "Bright Eyes",
            "title": "One For You, One For Me",
            "kids_safe": 0.81,
            "love": 0.0,
            "mood": 0.045,
            "length": 0.21,
            "complexity": 0.23
        },
        {
            "id": 858,
            "artist": "Glashaus",
            "title": "Wenn das Liebe Ist (Director's Cut)",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.055,
            "length": 0.25,
            "complexity": 0.45
        },
        {
            "id": 930,
            "artist": "Hunters & Collectors",
            "title": "Inside a Fireball",
            "kids_safe": 0.45,
            "love": 0.02,
            "mood": 0.215,
            "length": 0.3,
            "complexity": 0.37
        },
        {
            "id": 168,
            "artist": "The Heptones",
            "title": "Why Must I",
            "kids_safe": 0.96,
            "love": 0.09,
            "mood": 1.0,
            "length": 0.22,
            "complexity": 0.23
        },
        {
            "id": 692,
            "artist": "Sade",
            "title": "I Never Thought I'd See the Day",
            "kids_safe": 0.96,
            "love": 0.12,
            "mood": 0.99,
            "length": 0.12,
            "complexity": 0.25
        },
        {
            "id": 728,
            "artist": "Ronnie Grey",
            "title": "Love Will Keep Us Together",
            "kids_safe": 0.91,
            "love": 0.46,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.33
        },
        {
            "id": 35,
            "artist": "Keith Thompson",
            "title": "Strange Brew",
            "kids_safe": 0.92,
            "love": 0.06,
            "mood": 0.015,
            "length": 0.1,
            "complexity": 0.47
        },
        {
            "id": 393,
            "artist": "Vico Torriani",
            "title": "Santa Lucia",
            "kids_safe": 0.76,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.14,
            "complexity": 0.71
        },
        {
            "id": 362,
            "artist": "Giacomo Gates",
            "title": "It's the Talk of the Town",
            "kids_safe": 0.96,
            "love": 0.1,
            "mood": 0.995,
            "length": 0.2,
            "complexity": 0.35
        },
        {
            "id": 273,
            "artist": "Everlast",
            "title": "Kill the Emperor",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.0,
            "length": 0.28,
            "complexity": 0.49
        },
        {
            "id": 418,
            "artist": "Leonard Cohen",
            "title": "The Partisan [Hartwall Arena, Helsinki, Finland, October 10, 2008]",
            "kids_safe": 0.34,
            "love": 0.05,
            "mood": 0.27,
            "length": 0.27,
            "complexity": 0.48
        },
        {
            "id": 691,
            "artist": "Pee Wee Russell",
            "title": "If I Had You",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.21,
            "complexity": 0.19
        },
        {
            "id": 253,
            "artist": "Alestorm",
            "title": "The Quest",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.15,
            "complexity": 0.37
        },
        {
            "id": 942,
            "artist": "Sarah Blasko",
            "title": "All I Want",
            "kids_safe": 0.71,
            "love": 0.04,
            "mood": 0.05,
            "length": 0.18,
            "complexity": 0.3
        },
        {
            "id": 249,
            "artist": "Willis \"Gator\" Jackson",
            "title": "It's Too Late",
            "kids_safe": 0.06,
            "love": 0.06,
            "mood": 0.045,
            "length": 0.23,
            "complexity": 0.31
        },
        {
            "id": 572,
            "artist": "Bee Gees",
            "title": "Turn Around, Look at Me",
            "kids_safe": 0.99,
            "love": 0.19,
            "mood": 0.93,
            "length": 0.13,
            "complexity": 0.23
        },
        {
            "id": 219,
            "artist": "Britney Spears",
            "title": "Don't Cry",
            "kids_safe": 0.83,
            "love": 0.14,
            "mood": 0.0,
            "length": 0.3,
            "complexity": 0.21
        },
        {
            "id": 104,
            "artist": "Buy This Song",
            "title": "The Zoo",
            "kids_safe": 0.67,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.17,
            "complexity": 0.27
        },
        {
            "id": 798,
            "artist": "Charles Aznavour",
            "title": "Il Faut Savoir",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.16,
            "complexity": 0.63
        },
        {
            "id": 301,
            "artist": "John Lee Hooker",
            "title": "Boom Boom",
            "kids_safe": 0.2,
            "love": 0.05,
            "mood": 0.99,
            "length": 0.12,
            "complexity": 0.4
        },
        {
            "id": 210,
            "artist": "Buy This Song",
            "title": "Sophisticated Lady",
            "kids_safe": 0.53,
            "love": 0.06,
            "mood": 1.0,
            "length": 0.2,
            "complexity": 0.3
        },
        {
            "id": 243,
            "artist": "Scott Walker",
            "title": "All I Do Is Dream of You",
            "kids_safe": 1.0,
            "love": 0.09,
            "mood": 0.96,
            "length": 0.16,
            "complexity": 0.23
        },
        {
            "id": 996,
            "artist": "Triumph",
            "title": "A  World of Fantasy",
            "kids_safe": 0.2,
            "love": 0.03,
            "mood": 0.22,
            "length": 0.29,
            "complexity": 0.22
        },
        {
            "id": 149,
            "artist": "Tony Messina",
            "title": "Green Dolphin Street",
            "kids_safe": 1.0,
            "love": 0.24,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.37
        },
        {
            "id": 100,
            "artist": "Foo Fighters",
            "title": "Home",
            "kids_safe": 0.99,
            "love": 0.06,
            "mood": 0.925,
            "length": 0.13,
            "complexity": 0.38
        },
        {
            "id": 819,
            "artist": "Junie C. Cobb",
            "title": "Just Squeeze Me (But Don't Tease Me)",
            "kids_safe": 0.9,
            "love": 0.23,
            "mood": 1.0,
            "length": 0.21,
            "complexity": 0.19
        },
        {
            "id": 802,
            "artist": "Melanie Martinez",
            "title": "Milk and Cookies",
            "kids_safe": 0.01,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.21,
            "complexity": 0.36
        },
        {
            "id": 120,
            "artist": "Barrington Levy",
            "title": "She's Mine",
            "kids_safe": 1.0,
            "love": 0.57,
            "mood": 1.0,
            "length": 0.51,
            "complexity": 0.1
        },
        {
            "id": 202,
            "artist": "Prince Nico Mbarga",
            "title": "Sweet Mother",
            "kids_safe": 0.0,
            "love": 0.14,
            "mood": 0.01,
            "length": 0.32,
            "complexity": 0.21
        },
        {
            "id": 745,
            "artist": "Busta Rhymes",
            "title": "Where's My Money",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.55,
            "complexity": 0.41
        },
        {
            "id": 357,
            "artist": "Vic Damone",
            "title": "Among My Souvenirs",
            "kids_safe": 1.0,
            "love": 0.17,
            "mood": 0.525,
            "length": 0.09,
            "complexity": 0.34
        },
        {
            "id": 509,
            "artist": "Sunrise Avenue",
            "title": "Fairytale Gone Bad [Radio Edit]",
            "kids_safe": 0.02,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.34,
            "complexity": 0.22
        },
        {
            "id": 226,
            "artist": "Paulina Rubio",
            "title": "Causa y Efecto",
            "kids_safe": 0.94,
            "love": 0.0,
            "mood": 0.895,
            "length": 0.24,
            "complexity": 0.39
        },
        {
            "id": 212,
            "artist": "Current 93",
            "title": "Black Flowers Please",
            "kids_safe": 0.45,
            "love": 0.02,
            "mood": 0.01,
            "length": 0.33,
            "complexity": 0.46
        },
        {
            "id": 543,
            "artist": "The Troggs",
            "title": "Little Girl",
            "kids_safe": 0.74,
            "love": 0.22,
            "mood": 0.995,
            "length": 0.2,
            "complexity": 0.32
        },
        {
            "id": 436,
            "artist": "Jefferson Airplane",
            "title": "The Other Side of This Life",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.77,
            "length": 0.23,
            "complexity": 0.18
        },
        {
            "id": 826,
            "artist": "Willie Nelson",
            "title": "On The Road Again",
            "kids_safe": 0.29,
            "love": 0.12,
            "mood": 0.99,
            "length": 0.13,
            "complexity": 0.26
        },
        {
            "id": 434,
            "artist": "Chris Norman",
            "title": "Midnight Lady",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.955,
            "length": 0.25,
            "complexity": 0.28
        },
        {
            "id": 162,
            "artist": "Controlled Bleeding",
            "title": "Untitled #2",
            "kids_safe": 0.78,
            "love": 0.17,
            "mood": 0.405,
            "length": 0.05,
            "complexity": 0.38
        },
        {
            "id": 963,
            "artist": "Wild Bill Davison",
            "title": "If I Had You [#]",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.21,
            "complexity": 0.19
        },
        {
            "id": 660,
            "artist": "Iron Maiden",
            "title": "Wildest Dreams",
            "kids_safe": 0.4,
            "love": 0.0,
            "mood": 0.525,
            "length": 0.23,
            "complexity": 0.27
        },
        {
            "id": 251,
            "artist": "Jim Nabors",
            "title": "The Little Drummer Boy",
            "kids_safe": 0.66,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.17,
            "complexity": 0.29
        },
        {
            "id": 102,
            "artist": "Nat King Cole",
            "title": "(I Love You) For Sentimental Reasons",
            "kids_safe": 1.0,
            "love": 0.73,
            "mood": 0.995,
            "length": 0.1,
            "complexity": 0.3
        },
        {
            "id": 713,
            "artist": "Sha Na Na",
            "title": "Come Go with Me",
            "kids_safe": 0.58,
            "love": 0.07,
            "mood": 0.985,
            "length": 0.23,
            "complexity": 0.15
        },
        {
            "id": 506,
            "artist": "Crime Mob",
            "title": "Crunk Inc.",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.42,
            "complexity": 0.46
        },
        {
            "id": 489,
            "artist": "Wedlock",
            "title": "Discopharma [Original 7\" Mix]",
            "kids_safe": 0.99,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.22,
            "complexity": 0.41
        },
        {
            "id": 654,
            "artist": "Ellie Goulding",
            "title": "Devotion",
            "kids_safe": 0.82,
            "love": 0.11,
            "mood": 0.83,
            "length": 0.29,
            "complexity": 0.18
        },
        {
            "id": 283,
            "artist": "Lou Bega",
            "title": "You Wanna Be Americano [El Camino Album Edit]",
            "kids_safe": 0.48,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.32,
            "complexity": 0.23
        },
        {
            "id": 215,
            "artist": "Pablo Albor\u00e1n",
            "title": "Ser\u00e9",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.085,
            "length": 0.21,
            "complexity": 0.41
        },
        {
            "id": 337,
            "artist": "Ian Dury & the Blockheads",
            "title": "Wake Up and Make Love With Me",
            "kids_safe": 0.31,
            "love": 0.36,
            "mood": 1.0,
            "length": 0.24,
            "complexity": 0.28
        },
        {
            "id": 994,
            "artist": "Do or Die",
            "title": "Alpha and Omega",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.0,
            "length": 0.52,
            "complexity": 0.37
        },
        {
            "id": 611,
            "artist": "Hampton String Quartet",
            "title": "Let It Snow! Let It Snow! Let It Snow!",
            "kids_safe": 0.91,
            "love": 0.11,
            "mood": 0.345,
            "length": 0.12,
            "complexity": 0.44
        },
        {
            "id": 53,
            "artist": "Art Farmer",
            "title": "Killer Joe",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.965,
            "length": 0.15,
            "complexity": 0.52
        },
        {
            "id": 514,
            "artist": "Infected Mushroom",
            "title": "Cities of the Future",
            "kids_safe": 0.93,
            "love": 0.11,
            "mood": 0.785,
            "length": 0.06,
            "complexity": 0.46
        },
        {
            "id": 111,
            "artist": "Agust\u00edn Lara",
            "title": "Mar\u00eda Bonita",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.35,
            "length": 0.15,
            "complexity": 0.71
        },
        {
            "id": 157,
            "artist": "The Supremes",
            "title": "I'm Gonna Let My Heart Do the Walking",
            "kids_safe": 1.0,
            "love": 0.19,
            "mood": 0.995,
            "length": 0.31,
            "complexity": 0.24
        },
        {
            "id": 455,
            "artist": "Mozez",
            "title": "So Still",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.82,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 795,
            "artist": "The Dominoes",
            "title": "Do It Again",
            "kids_safe": 1.0,
            "love": 0.2,
            "mood": 0.985,
            "length": 0.24,
            "complexity": 0.29
        },
        {
            "id": 774,
            "artist": "Anita O'Day",
            "title": "Ain't Misbehavin'",
            "kids_safe": 0.57,
            "love": 0.44,
            "mood": 0.99,
            "length": 0.15,
            "complexity": 0.26
        },
        {
            "id": 258,
            "artist": "Mitch Ryder",
            "title": "Jenny Take a Ride",
            "kids_safe": 0.78,
            "love": 0.04,
            "mood": 0.99,
            "length": 0.26,
            "complexity": 0.2
        },
        {
            "id": 743,
            "artist": "Georgie Fame & the Blue Flames",
            "title": "Sweet Thing",
            "kids_safe": 0.19,
            "love": 0.04,
            "mood": 0.995,
            "length": 0.54,
            "complexity": 0.15
        },
        {
            "id": 241,
            "artist": "Connie Francis",
            "title": "I'll Close My Eyes",
            "kids_safe": 0.93,
            "love": 0.17,
            "mood": 0.965,
            "length": 0.12,
            "complexity": 0.42
        },
        {
            "id": 329,
            "artist": "Damien Sargue",
            "title": "Aimer",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.835,
            "length": 0.17,
            "complexity": 0.29
        },
        {
            "id": 350,
            "artist": "O Zone",
            "title": "Despre Tine (Original Version)",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.745,
            "length": 0.11,
            "complexity": 0.62
        },
        {
            "id": 54,
            "artist": "Mich\u00e9le Ramo",
            "title": "The Song is You",
            "kids_safe": 1.0,
            "love": 0.2,
            "mood": 0.995,
            "length": 0.13,
            "complexity": 0.44
        },
        {
            "id": 820,
            "artist": "Kenny Drew",
            "title": "There Is No Greater Love",
            "kids_safe": 0.99,
            "love": 0.38,
            "mood": 0.995,
            "length": 0.11,
            "complexity": 0.23
        },
        {
            "id": 681,
            "artist": "Goodies",
            "title": "Wild Thing",
            "kids_safe": 1.0,
            "love": 0.35,
            "mood": 0.96,
            "length": 0.11,
            "complexity": 0.15
        },
        {
            "id": 935,
            "artist": "Belinda Carlisle",
            "title": "Vision of You",
            "kids_safe": 0.45,
            "love": 0.11,
            "mood": 0.975,
            "length": 0.14,
            "complexity": 0.45
        },
        {
            "id": 741,
            "artist": "Lale Andersen",
            "title": "Lili Marleen",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.075,
            "length": 0.24,
            "complexity": 0.51
        },
        {
            "id": 1,
            "artist": "Dead Kennedys",
            "title": "Police Truck",
            "kids_safe": 0.07,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.19,
            "complexity": 0.46
        },
        {
            "id": 223,
            "artist": "Percy Faith & His Orchestra",
            "title": "Theme from \"A Summer Place\"",
            "kids_safe": 1.0,
            "love": 0.29,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.36
        },
        {
            "id": 670,
            "artist": "Django Reinhardt",
            "title": "Moonglow",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.16,
            "complexity": 0.24
        },
        {
            "id": 790,
            "artist": "Andy Williams",
            "title": "Under Paris Skies",
            "kids_safe": 0.78,
            "love": 0.37,
            "mood": 0.995,
            "length": 0.17,
            "complexity": 0.34
        },
        {
            "id": 953,
            "artist": "Mariah Carey",
            "title": "We Belong Together",
            "kids_safe": 0.27,
            "love": 0.07,
            "mood": 0.025,
            "length": 0.45,
            "complexity": 0.33
        },
        {
            "id": 592,
            "artist": "Paradise Lost",
            "title": "Deus Misereatur (Intro)",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.945,
            "length": 0.21,
            "complexity": 0.55
        },
        {
            "id": 383,
            "artist": "Al Stewart",
            "title": "Year of the Cat",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.655,
            "length": 0.24,
            "complexity": 0.44
        },
        {
            "id": 850,
            "artist": "First Aid Kit",
            "title": "Waltz For Richard",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.075,
            "length": 0.16,
            "complexity": 0.42
        },
        {
            "id": 269,
            "artist": "Breach of Trust",
            "title": "Disease",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.18,
            "complexity": 0.38
        },
        {
            "id": 400,
            "artist": "Doctor E",
            "title": "Here's That Rainy Day",
            "kids_safe": 0.93,
            "love": 0.17,
            "mood": 0.995,
            "length": 0.08,
            "complexity": 0.36
        },
        {
            "id": 767,
            "artist": "Chick Corea",
            "title": "My One and Only Love",
            "kids_safe": 1.0,
            "love": 0.24,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.45
        },
        {
            "id": 907,
            "artist": "Uli",
            "title": "Simple",
            "kids_safe": 0.97,
            "love": 0.04,
            "mood": 0.93,
            "length": 0.22,
            "complexity": 0.28
        },
        {
            "id": 588,
            "artist": "Frankie Ruiz",
            "title": "Mi Libertad",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.78,
            "length": 0.34,
            "complexity": 0.28
        },
        {
            "id": 52,
            "artist": "Soft Machine",
            "title": "Hibou Anemone & Bear",
            "kids_safe": 0.98,
            "love": 0.07,
            "mood": 0.625,
            "length": 0.1,
            "complexity": 0.46
        },
        {
            "id": 732,
            "artist": "Doris Day",
            "title": "With a Song in My Heart",
            "kids_safe": 0.97,
            "love": 0.24,
            "mood": 0.985,
            "length": 0.1,
            "complexity": 0.36
        },
        {
            "id": 45,
            "artist": "Lady Saw",
            "title": "Been So Long",
            "kids_safe": 0.85,
            "love": 0.13,
            "mood": 0.29,
            "length": 0.41,
            "complexity": 0.26
        },
        {
            "id": 278,
            "artist": "George Shearing",
            "title": "High on a Windy Hill",
            "kids_safe": 0.96,
            "love": 0.24,
            "mood": 0.92,
            "length": 0.1,
            "complexity": 0.37
        },
        {
            "id": 675,
            "artist": "Randy Travis",
            "title": "Three Wooden Crosses [*]",
            "kids_safe": 0.94,
            "love": 0.04,
            "mood": 0.99,
            "length": 0.32,
            "complexity": 0.34
        },
        {
            "id": 883,
            "artist": "Armand Van Helden",
            "title": "Witch Doktor",
            "kids_safe": 0.0,
            "love": 0.03,
            "mood": 0.005,
            "length": 0.69,
            "complexity": 0.3
        },
        {
            "id": 984,
            "artist": "Gram Parsons",
            "title": "Streets of Baltimore",
            "kids_safe": 1.0,
            "love": 0.12,
            "mood": 0.995,
            "length": 0.2,
            "complexity": 0.37
        },
        {
            "id": 851,
            "artist": "Helen Humes",
            "title": "Jet Propelled Papa",
            "kids_safe": 0.99,
            "love": 0.04,
            "mood": 0.96,
            "length": 0.16,
            "complexity": 0.4
        },
        {
            "id": 306,
            "artist": "Lightnin' Hopkins",
            "title": "Everything Happens to Me",
            "kids_safe": 0.27,
            "love": 0.12,
            "mood": 0.76,
            "length": 0.19,
            "complexity": 0.48
        },
        {
            "id": 948,
            "artist": "Sean Paul",
            "title": "My Name",
            "kids_safe": 0.78,
            "love": 0.17,
            "mood": 0.99,
            "length": 0.26,
            "complexity": 0.47
        },
        {
            "id": 609,
            "artist": "Bobby Womack",
            "title": "Save the Children",
            "kids_safe": 0.23,
            "love": 0.07,
            "mood": 1.0,
            "length": 0.42,
            "complexity": 0.34
        },
        {
            "id": 339,
            "artist": "Black Box",
            "title": "Everybody Everybody",
            "kids_safe": 0.82,
            "love": 0.15,
            "mood": 0.99,
            "length": 0.27,
            "complexity": 0.23
        },
        {
            "id": 905,
            "artist": "Kirsty MacColl",
            "title": "There's a Guy Works Down the Chip Shop Swears He's Elvis [Country Versi",
            "kids_safe": 0.75,
            "love": 0.0,
            "mood": 0.205,
            "length": 0.31,
            "complexity": 0.25
        },
        {
            "id": 557,
            "artist": "Rocket from the Tombs",
            "title": "Search & Destroy",
            "kids_safe": 0.99,
            "love": 0.07,
            "mood": 0.025,
            "length": 0.16,
            "complexity": 0.35
        },
        {
            "id": 295,
            "artist": "Mark Knopfler",
            "title": "Laughs and Jokes and Drinks and Smokes",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.27,
            "complexity": 0.36
        },
        {
            "id": 803,
            "artist": "Kasabian",
            "title": "Cutt Off",
            "kids_safe": 0.51,
            "love": 0.0,
            "mood": 0.96,
            "length": 0.18,
            "complexity": 0.42
        },
        {
            "id": 119,
            "artist": "Retros",
            "title": "Bad to Me",
            "kids_safe": 0.98,
            "love": 0.06,
            "mood": 0.14,
            "length": 0.14,
            "complexity": 0.32
        },
        {
            "id": 674,
            "artist": "Parachute",
            "title": "The New Year",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.96,
            "length": 0.36,
            "complexity": 0.27
        },
        {
            "id": 110,
            "artist": "Toots Thielemans",
            "title": "Autumn Leaves",
            "kids_safe": 0.97,
            "love": 0.09,
            "mood": 0.83,
            "length": 0.11,
            "complexity": 0.7
        },
        {
            "id": 244,
            "artist": "Brian McKnight",
            "title": "Shoulda, Woulda, Coulda",
            "kids_safe": 0.62,
            "love": 0.03,
            "mood": 1.0,
            "length": 0.47,
            "complexity": 0.25
        },
        {
            "id": 26,
            "artist": "Udo Lindenberg",
            "title": "Alles Klar auf der Andrea Doria",
            "kids_safe": 0.89,
            "love": 0.0,
            "mood": 0.025,
            "length": 0.19,
            "complexity": 0.66
        },
        {
            "id": 748,
            "artist": "The Bryan Ferry Orchestra",
            "title": "This Island Earth",
            "kids_safe": 0.84,
            "love": 0.04,
            "mood": 0.94,
            "length": 0.15,
            "complexity": 0.55
        },
        {
            "id": 330,
            "artist": "Mariah Carey",
            "title": "Auld Lang Syne (The New Year's Anthem)",
            "kids_safe": 0.98,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.22,
            "complexity": 0.24
        },
        {
            "id": 587,
            "artist": "The Pussycat Dolls",
            "title": "Don't Cha",
            "kids_safe": 0.0,
            "love": 0.08,
            "mood": 1.0,
            "length": 0.64,
            "complexity": 0.34
        },
        {
            "id": 280,
            "artist": "Illy",
            "title": "Riptide",
            "kids_safe": 0.71,
            "love": 0.1,
            "mood": 0.99,
            "length": 0.37,
            "complexity": 0.2
        },
        {
            "id": 457,
            "artist": "Joseph Arthur",
            "title": "Space Needle",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 667,
            "artist": "Amos Lee",
            "title": "Say Goodbye",
            "kids_safe": 0.75,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.2,
            "complexity": 0.21
        },
        {
            "id": 144,
            "artist": "The Midway State",
            "title": "Nobody Understands",
            "kids_safe": 0.9,
            "love": 0.12,
            "mood": 0.98,
            "length": 0.32,
            "complexity": 0.25
        },
        {
            "id": 866,
            "artist": "Beastie Boys",
            "title": "Jimi",
            "kids_safe": 0.12,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.09,
            "complexity": 0.49
        },
        {
            "id": 828,
            "artist": "Ibrahim Ferrer",
            "title": "Ay Candela",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.16,
            "complexity": 0.6
        },
        {
            "id": 796,
            "artist": "The Dixie Cups",
            "title": "Iko Iko",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.19,
            "complexity": 0.23
        },
        {
            "id": 158,
            "artist": "Zion I",
            "title": "Coastin'",
            "kids_safe": 0.77,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.42,
            "complexity": 0.38
        },
        {
            "id": 794,
            "artist": "Kate Bush",
            "title": "Wuthering Heights",
            "kids_safe": 0.88,
            "love": 0.05,
            "mood": 0.05,
            "length": 0.28,
            "complexity": 0.29
        },
        {
            "id": 940,
            "artist": "Bert Kaempfert",
            "title": "Afrikaan Beat",
            "kids_safe": 0.77,
            "love": 0.09,
            "mood": 0.995,
            "length": 0.22,
            "complexity": 0.43
        },
        {
            "id": 599,
            "artist": "Frank Sinatra",
            "title": "The Girl Next Door",
            "kids_safe": 0.96,
            "love": 0.17,
            "mood": 0.85,
            "length": 0.13,
            "complexity": 0.45
        },
        {
            "id": 92,
            "artist": "Scorpions",
            "title": "Robot Man",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.17,
            "complexity": 0.23
        },
        {
            "id": 11,
            "artist": "Billy Currington",
            "title": "People Are Crazy",
            "kids_safe": 0.0,
            "love": 0.08,
            "mood": 0.895,
            "length": 0.26,
            "complexity": 0.43
        },
        {
            "id": 287,
            "artist": "The Kinks",
            "title": "Powerman",
            "kids_safe": 0.37,
            "love": 0.0,
            "mood": 0.64,
            "length": 0.24,
            "complexity": 0.36
        },
        {
            "id": 59,
            "artist": "Simple Minds",
            "title": "Ghostdancing",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.905,
            "length": 0.36,
            "complexity": 0.37
        },
        {
            "id": 884,
            "artist": "Boxcar Willie",
            "title": "Boxcar's My Home",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.93,
            "length": 0.13,
            "complexity": 0.27
        },
        {
            "id": 656,
            "artist": "Sleepwave",
            "title": "Replace Me",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.12,
            "length": 0.11,
            "complexity": 0.38
        },
        {
            "id": 722,
            "artist": "Slowdive",
            "title": "Rutti",
            "kids_safe": 0.79,
            "love": 0.07,
            "mood": 0.19,
            "length": 0.1,
            "complexity": 0.21
        },
        {
            "id": 752,
            "artist": "Cymande",
            "title": "Brothers on the Slide",
            "kids_safe": 0.09,
            "love": 0.0,
            "mood": 0.065,
            "length": 0.2,
            "complexity": 0.23
        },
        {
            "id": 116,
            "artist": "Art Blakey & the Jazz Messengers",
            "title": "It's You or No One",
            "kids_safe": 0.86,
            "love": 0.21,
            "mood": 0.3,
            "length": 0.14,
            "complexity": 0.27
        },
        {
            "id": 872,
            "artist": "Rockheart",
            "title": "Love Song",
            "kids_safe": 0.25,
            "love": 0.4,
            "mood": 0.66,
            "length": 0.03,
            "complexity": 0.38
        },
        {
            "id": 286,
            "artist": "Mary Witt",
            "title": "If You Don't Know Me by Now",
            "kids_safe": 0.87,
            "love": 0.16,
            "mood": 0.99,
            "length": 0.17,
            "complexity": 0.38
        },
        {
            "id": 191,
            "artist": "Vico C",
            "title": "Te Voy a Tomar",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.53,
            "complexity": 0.51
        },
        {
            "id": 62,
            "artist": "Boris Gardiner",
            "title": "I Want To Wake Up With You",
            "kids_safe": 0.98,
            "love": 0.23,
            "mood": 0.995,
            "length": 0.32,
            "complexity": 0.1
        },
        {
            "id": 16,
            "artist": "Luis Fonsi",
            "title": "Gritar [Video] [*][Multimedia Track]",
            "kids_safe": 0.53,
            "love": 0.0,
            "mood": 0.085,
            "length": 0.31,
            "complexity": 0.35
        },
        {
            "id": 711,
            "artist": "Buy This Song",
            "title": "America Medley",
            "kids_safe": 0.93,
            "love": 0.08,
            "mood": 0.985,
            "length": 0.27,
            "complexity": 0.23
        },
        {
            "id": 456,
            "artist": "Black M",
            "title": "On s'fait du mal",
            "kids_safe": 0.26,
            "love": 0.0,
            "mood": 0.095,
            "length": 0.28,
            "complexity": 0.36
        },
        {
            "id": 403,
            "artist": "Johnny Cash",
            "title": "Ring of Fire",
            "kids_safe": 1.0,
            "love": 0.1,
            "mood": 0.005,
            "length": 0.2,
            "complexity": 0.12
        },
        {
            "id": 371,
            "artist": "Humane",
            "title": "Rescue Me",
            "kids_safe": 0.98,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.27,
            "complexity": 0.36
        },
        {
            "id": 618,
            "artist": "John Vanderslice",
            "title": "Cool Purple Mist",
            "kids_safe": 0.88,
            "love": 0.05,
            "mood": 0.195,
            "length": 0.12,
            "complexity": 0.55
        },
        {
            "id": 451,
            "artist": "Charlie Spivak",
            "title": "Laura",
            "kids_safe": 0.96,
            "love": 0.24,
            "mood": 0.865,
            "length": 0.06,
            "complexity": 0.48
        },
        {
            "id": 888,
            "artist": "The Faders",
            "title": "Here with Me",
            "kids_safe": 0.88,
            "love": 0.07,
            "mood": 0.055,
            "length": 0.25,
            "complexity": 0.21
        },
        {
            "id": 121,
            "artist": "P\u00e9rez Prado",
            "title": "Mambo No. 5",
            "kids_safe": 0.25,
            "love": 0.05,
            "mood": 0.82,
            "length": 0.11,
            "complexity": 0.38
        },
        {
            "id": 646,
            "artist": "My Morning Jacket",
            "title": "Can You See the Hard Helmet on My Head?",
            "kids_safe": 0.82,
            "love": 0.05,
            "mood": 0.635,
            "length": 0.14,
            "complexity": 0.47
        },
        {
            "id": 460,
            "artist": "2 Chainz",
            "title": "Cut Her Off",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.43,
            "complexity": 0.29
        },
        {
            "id": 510,
            "artist": "Marley's Ghost",
            "title": "Leopard Skin Pillbox Hat",
            "kids_safe": 0.87,
            "love": 0.08,
            "mood": 0.995,
            "length": 0.26,
            "complexity": 0.32
        },
        {
            "id": 954,
            "artist": "Depeche Mode",
            "title": "Pleasure, Little Treasure [DVD][*][Mix]",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.18,
            "complexity": 0.23
        },
        {
            "id": 427,
            "artist": "Mission of Burma",
            "title": "Academy Fight Song",
            "kids_safe": 0.91,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.17,
            "complexity": 0.35
        },
        {
            "id": 952,
            "artist": "Hank Snow",
            "title": "Somewhere Along Life's Highway",
            "kids_safe": 0.99,
            "love": 0.09,
            "mood": 0.965,
            "length": 0.14,
            "complexity": 0.54
        },
        {
            "id": 444,
            "artist": "The Kinks",
            "title": "Lola",
            "kids_safe": 0.01,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.36,
            "complexity": 0.3
        },
        {
            "id": 813,
            "artist": "Mika",
            "title": "Grace Kelly",
            "kids_safe": 0.84,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.44,
            "complexity": 0.2
        },
        {
            "id": 659,
            "artist": "Otis Rush & His Band",
            "title": "Double Trouble",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.04,
            "length": 0.07,
            "complexity": 0.58
        },
        {
            "id": 281,
            "artist": "Dorsey Brothers Orchestra",
            "title": "Fine and Dandy",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.965,
            "length": 0.1,
            "complexity": 0.48
        },
        {
            "id": 695,
            "artist": "Scherrie",
            "title": "Baby Love",
            "kids_safe": 0.44,
            "love": 0.38,
            "mood": 1.0,
            "length": 0.23,
            "complexity": 0.33
        },
        {
            "id": 302,
            "artist": "Dolly Parton",
            "title": "Hold Me",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.96,
            "length": 0.16,
            "complexity": 0.28
        },
        {
            "id": 384,
            "artist": "Terry Callier",
            "title": "Live with Me",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.845,
            "length": 0.2,
            "complexity": 0.34
        },
        {
            "id": 309,
            "artist": "Helheim",
            "title": "Jormundgand",
            "kids_safe": 0.46,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.21,
            "complexity": 0.42
        },
        {
            "id": 724,
            "artist": "James Booker",
            "title": "Goodnight Sweetheart",
            "kids_safe": 1.0,
            "love": 0.08,
            "mood": 1.0,
            "length": 0.13,
            "complexity": 0.25
        },
        {
            "id": 671,
            "artist": "The Black Eyed Peas",
            "title": "Fallin' Up",
            "kids_safe": 0.19,
            "love": 0.03,
            "mood": 0.99,
            "length": 0.39,
            "complexity": 0.52
        },
        {
            "id": 893,
            "artist": "Jos\u00e9 Alfredo Jim\u00e9nez",
            "title": "Viejos Amigos",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.475,
            "length": 0.13,
            "complexity": 0.69
        },
        {
            "id": 14,
            "artist": "The Crash",
            "title": "Still Alive",
            "kids_safe": 0.52,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.19,
            "complexity": 0.33
        },
        {
            "id": 297,
            "artist": "Korn",
            "title": "It's On!",
            "kids_safe": 0.78,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.14,
            "complexity": 0.27
        },
        {
            "id": 129,
            "artist": "Ani DiFranco",
            "title": "Subdivision",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.155,
            "length": 0.26,
            "complexity": 0.49
        },
        {
            "id": 892,
            "artist": "The Charlatans UK",
            "title": "Title Fight",
            "kids_safe": 0.94,
            "love": 0.21,
            "mood": 1.0,
            "length": 0.29,
            "complexity": 0.23
        },
        {
            "id": 464,
            "artist": "Prince Fatty",
            "title": "Milk & Honey",
            "kids_safe": 0.99,
            "love": 0.05,
            "mood": 0.535,
            "length": 0.14,
            "complexity": 0.36
        },
        {
            "id": 923,
            "artist": "Hank Ballard",
            "title": "Annie Had a Baby",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.925,
            "length": 0.09,
            "complexity": 0.32
        },
        {
            "id": 941,
            "artist": "Viola Wills",
            "title": "If You Could Read My Mind",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.995,
            "length": 0.31,
            "complexity": 0.33
        },
        {
            "id": 928,
            "artist": "Spike Jones",
            "title": "Ramona",
            "kids_safe": 0.29,
            "love": 0.2,
            "mood": 0.99,
            "length": 0.22,
            "complexity": 0.27
        },
        {
            "id": 493,
            "artist": "Gotan Project",
            "title": "Vuelvo al Sur",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.92,
            "length": 0.12,
            "complexity": 0.38
        },
        {
            "id": 530,
            "artist": "Bud Tutmarc",
            "title": "Stardust",
            "kids_safe": 0.99,
            "love": 0.23,
            "mood": 0.93,
            "length": 0.16,
            "complexity": 0.46
        },
        {
            "id": 151,
            "artist": "Daft Punk",
            "title": "Human After All [\"Guy Man After All\"   Justice Remix]",
            "kids_safe": 0.2,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.2,
            "complexity": 0.0
        },
        {
            "id": 94,
            "artist": "Al Green",
            "title": "Call Me (Come Back Home)",
            "kids_safe": 0.93,
            "love": 0.03,
            "mood": 0.985,
            "length": 0.21,
            "complexity": 0.38
        },
        {
            "id": 112,
            "artist": "Sub Focus",
            "title": "Falling Down",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.06,
            "length": 0.06,
            "complexity": 0.04
        },
        {
            "id": 408,
            "artist": "Al Green",
            "title": "Let's Stay Together",
            "kids_safe": 0.93,
            "love": 0.18,
            "mood": 0.98,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 477,
            "artist": "Gabe Dixon",
            "title": "On a Day Just Like Today",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.33,
            "complexity": 0.24
        },
        {
            "id": 879,
            "artist": "Bobby Caldwell",
            "title": "Stay With Me",
            "kids_safe": 0.99,
            "love": 0.22,
            "mood": 0.845,
            "length": 0.17,
            "complexity": 0.43
        },
        {
            "id": 716,
            "artist": "Robey",
            "title": "One Night in Bangkok",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.9,
            "length": 0.43,
            "complexity": 0.38
        },
        {
            "id": 46,
            "artist": "Marvin Gaye",
            "title": "How Sweet It Is (To Be Loved by You)",
            "kids_safe": 0.84,
            "love": 0.67,
            "mood": 1.0,
            "length": 0.28,
            "complexity": 0.24
        },
        {
            "id": 235,
            "artist": "Syd Barrett",
            "title": "Golden Hair [Takes 5] [*][Take]",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.195,
            "length": 0.06,
            "complexity": 0.44
        },
        {
            "id": 965,
            "artist": "David DeMar\u00eda",
            "title": "Amores",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.805,
            "length": 0.17,
            "complexity": 0.63
        },
        {
            "id": 43,
            "artist": "The Mamas & the Papas",
            "title": "California Dreamin'",
            "kids_safe": 0.75,
            "love": 0.0,
            "mood": 0.955,
            "length": 0.21,
            "complexity": 0.3
        },
        {
            "id": 944,
            "artist": "The Bobs",
            "title": "White Room",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.165,
            "length": 0.17,
            "complexity": 0.46
        },
        {
            "id": 382,
            "artist": "Charlie Parker",
            "title": "Cherokee",
            "kids_safe": 0.96,
            "love": 0.18,
            "mood": 0.99,
            "length": 0.06,
            "complexity": 0.65
        },
        {
            "id": 44,
            "artist": "Sandi Thom",
            "title": "I Wish I Was a Punk Rocker (With Flowers in My Hair)",
            "kids_safe": 0.05,
            "love": 0.15,
            "mood": 0.975,
            "length": 0.37,
            "complexity": 0.23
        },
        {
            "id": 81,
            "artist": "V Ice",
            "title": "I Know",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.04,
            "length": 0.33,
            "complexity": 0.36
        },
        {
            "id": 130,
            "artist": "Les Paul",
            "title": "How High the Moon",
            "kids_safe": 0.99,
            "love": 0.26,
            "mood": 0.98,
            "length": 0.11,
            "complexity": 0.27
        },
        {
            "id": 854,
            "artist": "Suga Free",
            "title": "Secrets",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.995,
            "length": 0.97,
            "complexity": 0.32
        },
        {
            "id": 958,
            "artist": "The Velvet Underground",
            "title": "I'm Waiting for the Man",
            "kids_safe": 0.38,
            "love": 0.07,
            "mood": 0.98,
            "length": 0.19,
            "complexity": 0.44
        },
        {
            "id": 651,
            "artist": "Javier Sol\u00eds",
            "title": "En Mi Viejo San Juan",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.32,
            "length": 0.19,
            "complexity": 0.48
        },
        {
            "id": 417,
            "artist": "Big Daddy Kane",
            "title": "It's Hard Being The Kane",
            "kids_safe": 0.0,
            "love": 0.02,
            "mood": 0.01,
            "length": 0.91,
            "complexity": 0.39
        },
        {
            "id": 194,
            "artist": "J King y Maximan",
            "title": "Sr. Juez",
            "kids_safe": 0.12,
            "love": 0.0,
            "mood": 0.035,
            "length": 0.43,
            "complexity": 0.4
        },
        {
            "id": 473,
            "artist": "Staind",
            "title": "Open Your Eyes",
            "kids_safe": 0.53,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.17,
            "complexity": 0.52
        },
        {
            "id": 312,
            "artist": "Del Amitri",
            "title": "Hammering Heart",
            "kids_safe": 0.97,
            "love": 0.17,
            "mood": 0.99,
            "length": 0.27,
            "complexity": 0.4
        },
        {
            "id": 364,
            "artist": "No Use for a Name",
            "title": "On the Outside",
            "kids_safe": 0.98,
            "love": 0.1,
            "mood": 0.085,
            "length": 0.24,
            "complexity": 0.41
        },
        {
            "id": 18,
            "artist": "Butthole Surfers",
            "title": "Pepper",
            "kids_safe": 0.0,
            "love": 0.11,
            "mood": 0.835,
            "length": 0.35,
            "complexity": 0.26
        },
        {
            "id": 882,
            "artist": "Rupert Holmes",
            "title": "Annabella",
            "kids_safe": 0.98,
            "love": 0.13,
            "mood": 0.975,
            "length": 0.16,
            "complexity": 0.36
        },
        {
            "id": 549,
            "artist": "Buy This Song",
            "title": "Fixer Upper",
            "kids_safe": 1.0,
            "love": 0.09,
            "mood": 1.0,
            "length": 0.45,
            "complexity": 0.44
        },
        {
            "id": 957,
            "artist": "Billy Taylor",
            "title": "Blue Moon",
            "kids_safe": 1.0,
            "love": 0.47,
            "mood": 0.16,
            "length": 0.1,
            "complexity": 0.4
        },
        {
            "id": 124,
            "artist": "Buck Owens",
            "title": "Down on the Corner of Love",
            "kids_safe": 0.88,
            "love": 0.56,
            "mood": 0.995,
            "length": 0.18,
            "complexity": 0.24
        },
        {
            "id": 818,
            "artist": "Informatik",
            "title": "Watching You Watching Me",
            "kids_safe": 0.99,
            "love": 0.16,
            "mood": 0.94,
            "length": 0.09,
            "complexity": 0.43
        },
        {
            "id": 946,
            "artist": "Bad Manners",
            "title": "That'll Do Nicely",
            "kids_safe": 0.23,
            "love": 0.03,
            "mood": 0.98,
            "length": 0.25,
            "complexity": 0.37
        },
        {
            "id": 101,
            "artist": "Nina Nastasia",
            "title": "That's All There Is",
            "kids_safe": 0.56,
            "love": 0.0,
            "mood": 0.215,
            "length": 0.16,
            "complexity": 0.42
        },
        {
            "id": 132,
            "artist": "Yeah Yeah Yeahs",
            "title": "Subway",
            "kids_safe": 0.22,
            "love": 0.21,
            "mood": 0.41,
            "length": 0.25,
            "complexity": 0.13
        },
        {
            "id": 186,
            "artist": "Ian Campbell",
            "title": "I Think It's Going to Rain Today",
            "kids_safe": 0.99,
            "love": 0.07,
            "mood": 0.905,
            "length": 0.09,
            "complexity": 0.41
        },
        {
            "id": 392,
            "artist": "Lighter Shade of Brown",
            "title": "Whatever You Want",
            "kids_safe": 1.0,
            "love": 0.02,
            "mood": 0.99,
            "length": 0.34,
            "complexity": 0.3
        },
        {
            "id": 199,
            "artist": "Junior Wells",
            "title": "Little by Little",
            "kids_safe": 0.2,
            "love": 0.25,
            "mood": 0.54,
            "length": 0.16,
            "complexity": 0.28
        },
        {
            "id": 757,
            "artist": "Patti Austin",
            "title": "In and Out of Love",
            "kids_safe": 1.0,
            "love": 0.33,
            "mood": 1.0,
            "length": 0.22,
            "complexity": 0.23
        },
        {
            "id": 633,
            "artist": "Woody Guthrie",
            "title": "Mean Talking Blues",
            "kids_safe": 0.0,
            "love": 0.03,
            "mood": 0.01,
            "length": 0.52,
            "complexity": 0.43
        },
        {
            "id": 807,
            "artist": "Robin Greenstein",
            "title": "Searching",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 0.955,
            "length": 0.14,
            "complexity": 0.52
        },
        {
            "id": 466,
            "artist": "Yellowcard",
            "title": "California",
            "kids_safe": 0.11,
            "love": 0.0,
            "mood": 0.5,
            "length": 0.23,
            "complexity": 0.21
        },
        {
            "id": 469,
            "artist": "Kristi Guillory",
            "title": "Lucille",
            "kids_safe": 0.86,
            "love": 0.17,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.3
        },
        {
            "id": 316,
            "artist": "Brenda Lee",
            "title": "I'm Learning About Love [*]",
            "kids_safe": 0.98,
            "love": 0.27,
            "mood": 1.0,
            "length": 0.23,
            "complexity": 0.19
        },
        {
            "id": 897,
            "artist": "Elefant",
            "title": "Don't Wait",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.09,
            "length": 0.17,
            "complexity": 0.29
        },
        {
            "id": 304,
            "artist": "DMX",
            "title": "Slippin'",
            "kids_safe": 0.0,
            "love": 0.03,
            "mood": 0.0,
            "length": 0.94,
            "complexity": 0.26
        },
        {
            "id": 331,
            "artist": "Rosemary Clooney",
            "title": "How Am I to Know?",
            "kids_safe": 0.59,
            "love": 0.39,
            "mood": 0.955,
            "length": 0.06,
            "complexity": 0.44
        },
        {
            "id": 189,
            "artist": "Ebony Eyez",
            "title": "Good Vibrations",
            "kids_safe": 0.0,
            "love": 0.06,
            "mood": 0.99,
            "length": 0.47,
            "complexity": 0.4
        },
        {
            "id": 544,
            "artist": "Guy & Ralna",
            "title": "Why Me",
            "kids_safe": 0.99,
            "love": 0.05,
            "mood": 0.99,
            "length": 0.14,
            "complexity": 0.31
        },
        {
            "id": 378,
            "artist": "Scooter",
            "title": "Jigga Jigga! [DVD]",
            "kids_safe": 0.55,
            "love": 0.05,
            "mood": 0.985,
            "length": 0.26,
            "complexity": 0.39
        },
        {
            "id": 505,
            "artist": "OneRepublic",
            "title": "Sucker Punch",
            "kids_safe": 0.21,
            "love": 0.0,
            "mood": 0.96,
            "length": 0.17,
            "complexity": 0.28
        },
        {
            "id": 643,
            "artist": "Eddy Raven",
            "title": "Shine Shine Shine",
            "kids_safe": 0.89,
            "love": 0.0,
            "mood": 0.895,
            "length": 0.29,
            "complexity": 0.21
        },
        {
            "id": 20,
            "artist": "Erykah Badu",
            "title": "Drama",
            "kids_safe": 0.96,
            "love": 0.07,
            "mood": 0.06,
            "length": 0.17,
            "complexity": 0.28
        },
        {
            "id": 87,
            "artist": "Albert Hammond, Jr.",
            "title": "Postal Blowfish",
            "kids_safe": 0.99,
            "love": 0.06,
            "mood": 0.625,
            "length": 0.12,
            "complexity": 0.47
        },
        {
            "id": 321,
            "artist": "Judy Albanese",
            "title": "Love's Here (At Last) [Kupper's Sweet Vocal]",
            "kids_safe": 0.99,
            "love": 0.22,
            "mood": 0.995,
            "length": 0.15,
            "complexity": 0.28
        },
        {
            "id": 887,
            "artist": "Gerald Albright",
            "title": "All This Love",
            "kids_safe": 0.83,
            "love": 0.47,
            "mood": 1.0,
            "length": 0.23,
            "complexity": 0.31
        },
        {
            "id": 977,
            "artist": "Caravan Palace",
            "title": "Suzy",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.955,
            "length": 0.11,
            "complexity": 0.13
        },
        {
            "id": 452,
            "artist": "Chet Atkins",
            "title": "Out of Nowhere",
            "kids_safe": 0.98,
            "love": 0.38,
            "mood": 0.98,
            "length": 0.06,
            "complexity": 0.46
        },
        {
            "id": 532,
            "artist": "Mother Mother",
            "title": "Alone and Sublime",
            "kids_safe": 0.37,
            "love": 0.04,
            "mood": 0.01,
            "length": 0.18,
            "complexity": 0.4
        },
        {
            "id": 932,
            "artist": "It's a Beautiful Day",
            "title": "White Bird",
            "kids_safe": 0.01,
            "love": 0.0,
            "mood": 0.01,
            "length": 0.17,
            "complexity": 0.3
        },
        {
            "id": 467,
            "artist": "Bloodhound Gang",
            "title": "Three Point One Four",
            "kids_safe": 0.0,
            "love": 0.05,
            "mood": 0.325,
            "length": 0.45,
            "complexity": 0.39
        },
        {
            "id": 22,
            "artist": "Beastie Boys",
            "title": "Jimi",
            "kids_safe": 0.12,
            "love": 0.0,
            "mood": 0.03,
            "length": 0.09,
            "complexity": 0.49
        },
        {
            "id": 422,
            "artist": "The Bristols",
            "title": "My Bonnie",
            "kids_safe": 0.18,
            "love": 0.0,
            "mood": 0.04,
            "length": 0.14,
            "complexity": 0.09
        },
        {
            "id": 501,
            "artist": "Buy This Song",
            "title": "Come Home with Me Baby (Explicit Lyrics)",
            "kids_safe": 0.39,
            "love": 0.03,
            "mood": 0.99,
            "length": 0.22,
            "complexity": 0.3
        },
        {
            "id": 628,
            "artist": "Kings of Tomorrow",
            "title": "Finally [East & Young Remix]",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.64,
            "length": 0.37,
            "complexity": 0.2
        },
        {
            "id": 906,
            "artist": "Judy Garland",
            "title": "Everybody Sing [From Broadway Melody of 1938]",
            "kids_safe": 1.0,
            "love": 0.07,
            "mood": 0.995,
            "length": 0.42,
            "complexity": 0.34
        },
        {
            "id": 75,
            "artist": "The Waterboys",
            "title": "When Will We Be Married [2013 Remaster]",
            "kids_safe": 0.65,
            "love": 0.0,
            "mood": 0.95,
            "length": 0.28,
            "complexity": 0.1
        },
        {
            "id": 231,
            "artist": "Tilly and the Wall",
            "title": "Brave Day",
            "kids_safe": 0.99,
            "love": 0.08,
            "mood": 0.86,
            "length": 0.16,
            "complexity": 0.52
        },
        {
            "id": 123,
            "artist": "The Family Dogg",
            "title": "A Way of Life",
            "kids_safe": 0.76,
            "love": 0.12,
            "mood": 0.99,
            "length": 0.26,
            "complexity": 0.3
        },
        {
            "id": 459,
            "artist": "Eloy",
            "title": "Age of Insanity",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 0.0,
            "length": 0.35,
            "complexity": 0.55
        },
        {
            "id": 652,
            "artist": "Chuck Jackson",
            "title": "I Don't Want to Cry",
            "kids_safe": 0.89,
            "love": 0.13,
            "mood": 0.99,
            "length": 0.17,
            "complexity": 0.32
        },
        {
            "id": 535,
            "artist": "K2",
            "title": "Der Berg Ruft",
            "kids_safe": 0.0,
            "love": 0.0,
            "mood": 0.0,
            "length": 0.54,
            "complexity": 0.26
        },
        {
            "id": 341,
            "artist": "The Velvets",
            "title": "I",
            "kids_safe": 0.99,
            "love": 0.51,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.28
        },
        {
            "id": 397,
            "artist": "Corina Bartra",
            "title": "You Don't Know What Love Is",
            "kids_safe": 0.39,
            "love": 0.61,
            "mood": 0.01,
            "length": 0.12,
            "complexity": 0.35
        },
        {
            "id": 723,
            "artist": "The Cure",
            "title": "Let's Go to Bed",
            "kids_safe": 0.31,
            "love": 0.07,
            "mood": 0.095,
            "length": 0.21,
            "complexity": 0.36
        },
        {
            "id": 379,
            "artist": "Ian Van Dahl",
            "title": "Castles in the Sky",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.96,
            "length": 0.1,
            "complexity": 0.25
        },
        {
            "id": 141,
            "artist": "The Hidden Stars",
            "title": "It Came Upon a Midnight Clear",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.935,
            "length": 0.09,
            "complexity": 0.57
        },
        {
            "id": 203,
            "artist": "Buy This Song",
            "title": "Scooby Doo, Where Are You? (TV Theme)",
            "kids_safe": 0.46,
            "love": 0.0,
            "mood": 0.84,
            "length": 0.12,
            "complexity": 0.34
        },
        {
            "id": 616,
            "artist": "Chet Baker",
            "title": "My Old Flame",
            "kids_safe": 1.0,
            "love": 0.1,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.23
        },
        {
            "id": 349,
            "artist": "Jerry Jeff Walker",
            "title": "Standin' at the Big Hotel",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.46,
            "length": 0.23,
            "complexity": 0.39
        },
        {
            "id": 862,
            "artist": "Ron Wood",
            "title": "1234",
            "kids_safe": 0.15,
            "love": 0.3,
            "mood": 0.005,
            "length": 0.19,
            "complexity": 0.15
        },
        {
            "id": 134,
            "artist": "BoySetsFire",
            "title": "Pure",
            "kids_safe": 0.7,
            "love": 0.08,
            "mood": 0.08,
            "length": 0.09,
            "complexity": 0.55
        },
        {
            "id": 327,
            "artist": "Paul Hopkins",
            "title": "When You're Smiling",
            "kids_safe": 0.89,
            "love": 0.08,
            "mood": 0.995,
            "length": 0.16,
            "complexity": 0.33
        },
        {
            "id": 787,
            "artist": "Milton Nascimento",
            "title": "Filho",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.71,
            "length": 0.12,
            "complexity": 0.7
        },
        {
            "id": 388,
            "artist": "The Anix",
            "title": "Sometimes",
            "kids_safe": 0.99,
            "love": 0.17,
            "mood": 0.98,
            "length": 0.2,
            "complexity": 0.21
        },
        {
            "id": 201,
            "artist": "Aqualung",
            "title": "Nothing Else Matters",
            "kids_safe": 0.91,
            "love": 0.09,
            "mood": 0.11,
            "length": 0.13,
            "complexity": 0.36
        },
        {
            "id": 601,
            "artist": "Steely Dan",
            "title": "Do It Again",
            "kids_safe": 0.88,
            "love": 0.03,
            "mood": 0.82,
            "length": 0.23,
            "complexity": 0.33
        },
        {
            "id": 676,
            "artist": "Tom Paxton",
            "title": "I Give You the Morning",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.23,
            "complexity": 0.28
        },
        {
            "id": 240,
            "artist": "The Jeff Healey Band",
            "title": "Confidence Man",
            "kids_safe": 0.04,
            "love": 0.03,
            "mood": 0.995,
            "length": 0.24,
            "complexity": 0.39
        },
        {
            "id": 346,
            "artist": "Jennifer Weatherly",
            "title": "The Fine Art of Holding a Woman",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.955,
            "length": 0.15,
            "complexity": 0.23
        },
        {
            "id": 914,
            "artist": "Elvis Crespo",
            "title": "Mas Que Una Caricia",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.23,
            "complexity": 0.45
        },
        {
            "id": 196,
            "artist": "Sonic Blues",
            "title": "Shake Your Money Maker",
            "kids_safe": 0.25,
            "love": 0.1,
            "mood": 0.175,
            "length": 0.14,
            "complexity": 0.22
        },
        {
            "id": 107,
            "artist": "Gonzales",
            "title": "Too Long",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.35,
            "complexity": 0.1
        },
        {
            "id": 746,
            "artist": "Seabear",
            "title": "Arms",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.365,
            "length": 0.14,
            "complexity": 0.44
        },
        {
            "id": 877,
            "artist": "Jimmy Buffett*",
            "title": "Good Guys Win",
            "kids_safe": 0.54,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.3
        },
        {
            "id": 174,
            "artist": "George Gershwin",
            "title": "But Not for Me",
            "kids_safe": 0.11,
            "love": 0.2,
            "mood": 0.975,
            "length": 0.14,
            "complexity": 0.49
        },
        {
            "id": 918,
            "artist": "Ike & Tina Turner",
            "title": "Bold Soul Sister",
            "kids_safe": 0.77,
            "love": 0.0,
            "mood": 0.89,
            "length": 0.18,
            "complexity": 0.24
        },
        {
            "id": 432,
            "artist": "Roy Orbison",
            "title": "I'm Hurtin'",
            "kids_safe": 0.9,
            "love": 0.19,
            "mood": 0.18,
            "length": 0.08,
            "complexity": 0.41
        },
        {
            "id": 852,
            "artist": "Selena Gomez & the Scene",
            "title": "Who Says",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.4,
            "complexity": 0.2
        },
        {
            "id": 482,
            "artist": "Hot Water Music",
            "title": "Jack of All Trades",
            "kids_safe": 0.09,
            "love": 0.0,
            "mood": 0.12,
            "length": 0.09,
            "complexity": 0.55
        },
        {
            "id": 581,
            "artist": "The Specials",
            "title": "A Message to You Rudy",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.575,
            "length": 0.12,
            "complexity": 0.16
        },
        {
            "id": 865,
            "artist": "Glenn Miller",
            "title": "I've Got No Strings",
            "kids_safe": 0.99,
            "love": 0.26,
            "mood": 0.995,
            "length": 0.15,
            "complexity": 0.34
        },
        {
            "id": 420,
            "artist": "Moonlight Serenaders",
            "title": "Begin the Beguine",
            "kids_safe": 0.99,
            "love": 0.18,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.38
        },
        {
            "id": 744,
            "artist": "David Murray",
            "title": "You Don't Know What Love Is",
            "kids_safe": 0.39,
            "love": 0.61,
            "mood": 0.01,
            "length": 0.12,
            "complexity": 0.35
        },
        {
            "id": 894,
            "artist": "Django Reinhardt",
            "title": "Fine and Dandy",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.965,
            "length": 0.1,
            "complexity": 0.48
        },
        {
            "id": 143,
            "artist": "Patti LaBelle",
            "title": "You'll Never Walk Alone",
            "kids_safe": 0.97,
            "love": 0.2,
            "mood": 0.98,
            "length": 0.15,
            "complexity": 0.21
        },
        {
            "id": 308,
            "artist": "Buy This Song",
            "title": "Could You Use Me?",
            "kids_safe": 0.24,
            "love": 0.04,
            "mood": 0.975,
            "length": 0.34,
            "complexity": 0.45
        },
        {
            "id": 78,
            "artist": "James Kochalka Superstar",
            "title": "Hockey Monkey",
            "kids_safe": 0.18,
            "love": 0.09,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.21
        },
        {
            "id": 135,
            "artist": "Daft Punk",
            "title": "Technologic [Peaches No Logic Remix]",
            "kids_safe": 0.37,
            "love": 0.0,
            "mood": 0.475,
            "length": 0.14,
            "complexity": 0.48
        },
        {
            "id": 220,
            "artist": "De Danann",
            "title": "Danny Boy",
            "kids_safe": 0.65,
            "love": 0.09,
            "mood": 0.79,
            "length": 0.16,
            "complexity": 0.44
        },
        {
            "id": 342,
            "artist": "De De Pierce & His New Orleans Stompers",
            "title": "St. Louis Blues",
            "kids_safe": 0.88,
            "love": 0.28,
            "mood": 0.985,
            "length": 0.14,
            "complexity": 0.43
        },
        {
            "id": 195,
            "artist": "Hipmotism",
            "title": "Lonely Avenue",
            "kids_safe": 0.9,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.14,
            "complexity": 0.47
        },
        {
            "id": 781,
            "artist": "Bananarama",
            "title": "Some Girls",
            "kids_safe": 0.02,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.28,
            "complexity": 0.18
        },
        {
            "id": 547,
            "artist": "Jacques Brel",
            "title": "Le Moribond",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.485,
            "length": 0.43,
            "complexity": 0.22
        },
        {
            "id": 326,
            "artist": "Inner Circle",
            "title": "Bad Boys",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.0,
            "length": 0.46,
            "complexity": 0.13
        },
        {
            "id": 438,
            "artist": "Yuri",
            "title": "Vivir Sin Ti",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.005,
            "length": 0.18,
            "complexity": 0.41
        },
        {
            "id": 776,
            "artist": "Deliverance",
            "title": "No Love",
            "kids_safe": 0.42,
            "love": 0.46,
            "mood": 0.835,
            "length": 0.14,
            "complexity": 0.46
        },
        {
            "id": 458,
            "artist": "Red Lorry Yellow Lorry",
            "title": "This Today",
            "kids_safe": 0.95,
            "love": 0.0,
            "mood": 0.14,
            "length": 0.07,
            "complexity": 0.46
        },
        {
            "id": 696,
            "artist": "Kool & the Gang",
            "title": "Celebration",
            "kids_safe": 0.4,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.34,
            "complexity": 0.13
        },
        {
            "id": 508,
            "artist": "Slowdive",
            "title": "Rutti",
            "kids_safe": 0.79,
            "love": 0.07,
            "mood": 0.19,
            "length": 0.1,
            "complexity": 0.21
        },
        {
            "id": 693,
            "artist": "Maxine Weldon",
            "title": "But Beautiful",
            "kids_safe": 0.55,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.08,
            "complexity": 0.44
        },
        {
            "id": 927,
            "artist": "H.I.M.",
            "title": "Kiss the Void",
            "kids_safe": 0.67,
            "love": 0.0,
            "mood": 0.97,
            "length": 0.26,
            "complexity": 0.25
        },
        {
            "id": 439,
            "artist": "Jenni Rivera",
            "title": "Angel Baby",
            "kids_safe": 0.92,
            "love": 0.41,
            "mood": 0.995,
            "length": 0.12,
            "complexity": 0.39
        },
        {
            "id": 68,
            "artist": "Waylon Jennings",
            "title": "Pretend I Never Happened",
            "kids_safe": 0.9,
            "love": 0.15,
            "mood": 0.945,
            "length": 0.15,
            "complexity": 0.25
        },
        {
            "id": 232,
            "artist": "Jacqueline Ta\u00efeb",
            "title": "7 Heures du Matin",
            "kids_safe": 0.82,
            "love": 0.0,
            "mood": 0.515,
            "length": 0.24,
            "complexity": 0.45
        },
        {
            "id": 300,
            "artist": "Yves Montand",
            "title": "Le Gamin de Paris",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.165,
            "length": 0.23,
            "complexity": 0.61
        },
        {
            "id": 870,
            "artist": "Lead Belly",
            "title": "House Of The Rising Sun",
            "kids_safe": 0.98,
            "love": 0.03,
            "mood": 0.39,
            "length": 0.21,
            "complexity": 0.45
        },
        {
            "id": 916,
            "artist": "J. Stephen Howard",
            "title": "Dreams",
            "kids_safe": 1.0,
            "love": 0.06,
            "mood": 0.995,
            "length": 0.23,
            "complexity": 0.33
        },
        {
            "id": 317,
            "artist": "Perry Como",
            "title": "Hot Diggity (Dog Ziggity Boom)",
            "kids_safe": 0.19,
            "love": 0.14,
            "mood": 0.985,
            "length": 0.29,
            "complexity": 0.21
        },
        {
            "id": 978,
            "artist": "Cherry Ghost",
            "title": "People Help the People",
            "kids_safe": 0.0,
            "love": 0.19,
            "mood": 0.36,
            "length": 0.28,
            "complexity": 0.24
        },
        {
            "id": 106,
            "artist": "Alaska y Dinarama",
            "title": "A  Quien Le Importa",
            "kids_safe": 0.06,
            "love": 0.0,
            "mood": 0.065,
            "length": 0.25,
            "complexity": 0.3
        },
        {
            "id": 561,
            "artist": "Jethro Tull",
            "title": "No Lullaby",
            "kids_safe": 0.55,
            "love": 0.0,
            "mood": 0.015,
            "length": 0.19,
            "complexity": 0.49
        },
        {
            "id": 322,
            "artist": "DJ Smooth4Lyfe",
            "title": "Believe",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.965,
            "length": 0.34,
            "complexity": 0.16
        },
        {
            "id": 421,
            "artist": "Small Faces",
            "title": "Happydaystoytown",
            "kids_safe": 1.0,
            "love": 0.1,
            "mood": 1.0,
            "length": 0.28,
            "complexity": 0.3
        },
        {
            "id": 976,
            "artist": "Caetano Veloso",
            "title": "Domingo",
            "kids_safe": 0.29,
            "love": 0.0,
            "mood": 0.235,
            "length": 0.1,
            "complexity": 0.49
        },
        {
            "id": 97,
            "artist": "The Delfonics",
            "title": "La  La Means I Love You",
            "kids_safe": 1.0,
            "love": 0.11,
            "mood": 0.975,
            "length": 0.22,
            "complexity": 0.36
        },
        {
            "id": 267,
            "artist": "Athlete",
            "title": "Beautiful",
            "kids_safe": 0.96,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.15,
            "complexity": 0.18
        },
        {
            "id": 951,
            "artist": "Toquinho",
            "title": "Samba Em Prel\u00fadio",
            "kids_safe": 0.99,
            "love": 0.0,
            "mood": 0.975,
            "length": 0.11,
            "complexity": 0.65
        },
        {
            "id": 319,
            "artist": "The Saints Jazz Band",
            "title": "Tiger Rag",
            "kids_safe": 0.38,
            "love": 0.0,
            "mood": 0.05,
            "length": 0.12,
            "complexity": 0.16
        },
        {
            "id": 970,
            "artist": "Dionne Warwick",
            "title": "Don't Make Me Over",
            "kids_safe": 1.0,
            "love": 0.13,
            "mood": 0.985,
            "length": 0.23,
            "complexity": 0.12
        },
        {
            "id": 163,
            "artist": "The Band",
            "title": "Across the Great Divide",
            "kids_safe": 1.0,
            "love": 0.03,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.4
        },
        {
            "id": 574,
            "artist": "Hank Williams, Jr.",
            "title": "How's My Ex Treating You",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 0.315,
            "length": 0.12,
            "complexity": 0.32
        },
        {
            "id": 338,
            "artist": "Ohio Players",
            "title": "Whats Going on",
            "kids_safe": 0.9,
            "love": 0.0,
            "mood": 0.985,
            "length": 0.23,
            "complexity": 0.49
        },
        {
            "id": 36,
            "artist": "Fra Lippo Lippi",
            "title": "The Treasure",
            "kids_safe": 0.97,
            "love": 0.0,
            "mood": 0.115,
            "length": 0.08,
            "complexity": 0.66
        },
        {
            "id": 899,
            "artist": "Bobby Darin",
            "title": "Splish Splash",
            "kids_safe": 0.6,
            "love": 0.0,
            "mood": 0.99,
            "length": 0.23,
            "complexity": 0.39
        },
        {
            "id": 449,
            "artist": "Alkaline Trio",
            "title": "I Found Away",
            "kids_safe": 1.0,
            "love": 0.04,
            "mood": 0.025,
            "length": 0.21,
            "complexity": 0.41
        },
        {
            "id": 293,
            "artist": "Cesca",
            "title": "One",
            "kids_safe": 1.0,
            "love": 0.05,
            "mood": 0.99,
            "length": 0.29,
            "complexity": 0.22
        },
        {
            "id": 380,
            "artist": "Christophe",
            "title": "La  Petite Fille Du Soleil",
            "kids_safe": 0.25,
            "love": 0.0,
            "mood": 0.075,
            "length": 0.17,
            "complexity": 0.37
        },
        {
            "id": 263,
            "artist": "Dr. Alban",
            "title": "Sing Hallelujah! [Paradise Dub]",
            "kids_safe": 1.0,
            "love": 0.0,
            "mood": 1.0,
            "length": 0.17,
            "complexity": 0.22
        },
        {
            "id": 518,
            "artist": "Frances Gershwin",
            "title": "Love Is Here to Stay",
            "kids_safe": 0.99,
            "love": 0.28,
            "mood": 0.99,
            "length": 0.1,
            "complexity": 0.35
        },
        {
            "id": 841,
            "artist": "Aerosmith",
            "title": "Love in an Elevator [Live]",
            "kids_safe": 1.0,
            "love": 0.1,
            "mood": 1.0,
            "length": 0.31,
            "complexity": 0.29
        },
        {
            "id": 950,
            "artist": "Doc Watson",
            "title": "Shady Grove",
            "kids_safe": 0.98,
            "love": 0.27,
            "mood": 0.995,
            "length": 0.16,
            "complexity": 0.43
        },
        {
            "id": 683,
            "artist": "I Set My Friends on Fire",
            "title": "Brief Interviews with Hideous Men",
            "kids_safe": 0.79,
            "love": 0.0,
            "mood": 0.98,
            "length": 0.12,
            "complexity": 0.64
        },
        {
            "id": 98,
            "artist": "Bob Marley & the Wailers",
            "title": "Lively Up Yourself",
            "kids_safe": 0.16,
            "love": 0.0,
            "mood": 0.995,
            "length": 0.19,
            "complexity": 0.24
        },
        {
            "id": 285,
            "artist": "Magoo",
            "title": "Cop That Sh*t",
            "kids_safe": 0.0,
            "love": 0.01,
            "mood": 0.805,
            "length": 0.6,
            "complexity": 0.45
        },
        {
            "id": 810,
            "artist": "The Bobs",
            "title": "Elwood Decker",
            "kids_safe": 0.93,
            "love": 0.0,
            "mood": 0.02,
            "length": 0.06,
            "complexity": 0.54
        },
        {
            "id": 709,
            "artist": "Paw",
            "title": "Jessie",
            "kids_safe": 0.0,
            "love": 0.03,
            "mood": 1.0,
            "length": 0.22,
            "complexity": 0.2
        },
        {
            "id": 204,
            "artist": "Michael Mind",
            "title": "Show Me Love",
            "kids_safe": 0.99,
            "love": 0.41,
            "mood": 1.0,
            "length": 0.14,
            "complexity": 0.36
        },
        {
            "id": 715,
            "artist": "Buy This Song",
            "title": "O Little Town of Bethlehem",
            "kids_safe": 0.63,
            "love": 0.09,
            "mood": 0.96,
            "length": 0.13,
            "complexity": 0.39
        },
        {
            "id": 399,
            "artist": "Chico Hamilton",
            "title": "September Song",
            "kids_safe": 0.98,
            "love": 0.0,
            "mood": 0.95,
            "length": 0.06,
            "complexity": 0.46
        }
    ]
}				      
```
## Proposals for enhancement

Pull requests are welcome. For major changes, please open an issue first to discuss what you would 
like to change. 
Please make sure to update tests as appropriate.

## Copyright and License Information


Copyright (c) 2019 [Papaioannou Alexandros](https://www.linkedin.com/in/apapaio/), Shipley Kyle.  All rights reserved.

All trademarks referenced herein are property of their respective holders.

## Acknowledgments

* Prof. Paul Logston, Columbia University, Spring 2019
* Teaching Assistant Ms. Peiying Yu, Columbia University, Spring 2019

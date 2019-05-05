# TFA_Project
Tools for Analytics Final Project
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

1. artists_list() # returns a list with the unique set of artists that are associated with the lyrics text files 

2. raw_filenames_list() # returns a list with all the filenames of the lyrics text files of the folder named “Lyrics”

3. artist_s_songs_list(str)  # returns a list with all the filenames of the the lyrics text files that are associated with the artist that is passed as a string (str) to the function
	i.e. artist_s_songs_list("The Beatles") # returns ['860~Get Back~The Beatles.txt', '629~From Me to You~The Beatles.txt']

4. artist_s_cleaned_songs_list(str)  # returns a list with all the filenames of the the “cleaned” lyrics text files that are associated with the artist that is passed as a string (str) to the function
	i.e. artist_s_cleaned_songs_list("The Beatles") # returns ['cleaned_860~Get Back~The Beatles.txt',
 'cleaned_629~From Me to You~The Beatles.txt']

5. 

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Alexandros Papaioannou](https://www.linkedin.com/in/apapaio/)
[Kyle Shipley]

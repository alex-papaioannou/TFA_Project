#!/usr/bin/env python
# coding: utf-8

import main_optimized as m
import unittest
import time

# %%time
# cell_s_t = time.time()
    
#     parser = argparse.ArgumentParser('Parses the given directory of lyrics')
#     parser.add_argument('dir_given', help='Directory of the lyrics')
#     args = parser.parse_args()
#     dir_given = args.dir_given

#Simulated 'Given' directory, needs to be changed to input from command line kss0416
# dir_given = r'C:\Users\Kyle_Shipley\Documents\Columbia_Docs\IEOR 4501\ProjectTemp\TFA_Project-Alex2\TFA_Project-Alex\Lyrics'

#Unit Testing File

#import main.py as m

#check that title for song 997 is correct
#global raw_filenames_list_, profanity_score_min, profanity_score_max, love_score_min, love_score_max, mood_score_min, mood_score_max, length_score_min, length_score_max, complexity_score_min, complexity_score_max


class TestFuncOutputs(unittest.TestCase):

    def test_art_list(self):
        artists_list_ = m.artists_list()
        self.assertTrue(isinstance(artists_list_, list))
        
    def test_raw_list(self):
        raw_filenames_list_ = m.raw_filenames_list()
        self.assertTrue(isinstance(raw_filenames_list_, list))
        
    def test_artist_s_songs_list(self):
        self.assertEqual(len(m.artist_s_songs_list("Buy-This-Song")), 23)
        
#     def test_cleaning(self):
#         song_cleaning()
#         self.assertTrue(os.path.exists(dir_given + '/Cleaned_Songs/' + "cleaned_688~I Wanna Be Loved~Buy This Song.txt"))

    def test_artist_s_cleaned_songs_list(self):
        print()
        self.assertEqual(len(m.artist_s_cleaned_songs_list("Buy-This-Song")), 23)
 
    def test_ids(self):
        self.assertEqual(m.id_song_to_be_scored('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt'), 688)
 
    def test_artist(self):
        self.assertEqual(m.artist_song_to_be_scored('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt'), "Buy-This-Song")
         
    def test_title(self):
        self.assertEqual(m.title_song_to_be_scored('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt'), "I-Wanna-Be-Loved")
         
    def test_kid_safe(self):
        min_prof, max_prof = m.profanity_score_min_max()
        self.assertEqual(m.profanity_score('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt', min_prof, max_prof), 0.9683)
        
    def test_love(self):
        love_score_min, love_score_max = m.love_score_min_max()
        self.assertEqual(m.love_score('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt', love_score_min, love_score_max), 0.4536)
         
    def test_mood(self):
        mood_score_min, mood_score_max = m.mood_score_min_max()
        self.assertEqual(m.mood_score('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt', mood_score_min, mood_score_max), 1.0)
         
    def test_length(self):
        length_score_min, length_score_max = m.length_score_min_max()
        self.assertEqual(m.length_score('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt', length_score_min, length_score_max), 0.17)
         
    def test_complexity(self):
        complexity_score_min, complexity_score_max = m.complexity_score_min_max()
        self.assertEqual(m.complexity_score('cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt', complexity_score_min, complexity_score_max), 0.27)

def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFuncOutputs)
    unittest.TextTestRunner().run(suite)
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Runtime is:", time.time() - start_time)


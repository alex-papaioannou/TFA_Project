#!/usr/bin/env python
# coding: utf-8

import main as m
import unittest
import time
import os

# A directory with two songs for testing is used to test main


class TestFuncOutputs(unittest.TestCase):

    def test_art_list(self):
        artists_list_ = m.artists_list(test_dir)
        self.assertTrue(isinstance(artists_list_, list))

    def test_raw_list(self):
        raw_filenames_list_ = m.raw_filenames_list(test_dir)
        self.assertTrue(isinstance(raw_filenames_list_, list))

    def test_artist_s_songs_list(self):
        self.assertEqual(len(m.artist_s_songs_list("Raffi", test_dir)), 1)

    def test_cleaning(self):
        m.song_cleaning(test_dir)
        self.assertTrue(True)

    def test_artist_s_cleaned_songs_list(self):
        self.assertEqual(
            len(m.artist_s_cleaned_songs_list("Raffi", test_dir)), 1)

    def test_ids(self):
        self.assertEqual(m.id_song_to_be_scored(
            'cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt'), 688)

    def test_artist(self):
        self.assertEqual(m.artist_song_to_be_scored(
            'cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt'), "Buy This Song")

    def test_title(self):
        self.assertEqual(m.title_song_to_be_scored(
            'cleaned_688~Buy-This-Song~I-Wanna-Be-Loved.txt'), "I Wanna Be Loved")

    def test_kid_safe(self):
        min_prof, max_prof = m.profanity_score_min_max(test_dir)
        self.assertEqual(m.profanity_score(
            'cleaned_1001~Raffi~Wheels-on-the-Bus.txt', min_prof, max_prof, test_dir), 1.0)

    def test_love(self):
        love_score_min, love_score_max = m.love_score_min_max(test_dir)
        self.assertEqual(m.love_score('cleaned_1001~Raffi~Wheels-on-the-Bus.txt',
                                      love_score_min, love_score_max, test_dir), 0.0)

    def test_mood(self):
        mood_score_min, mood_score_max = m.mood_score_min_max(test_dir)
        self.assertEqual(m.mood_score('cleaned_1001~Raffi~Wheels-on-the-Bus.txt',
                                      mood_score_min, mood_score_max, test_dir), 1.0)

    def test_length(self):
        length_score_min, length_score_max = m.length_score_min_max(test_dir)
        self.assertEqual(m.length_score('cleaned_1001~Raffi~Wheels-on-the-Bus.txt',
                                        length_score_min, length_score_max, test_dir), 0.0)

    def test_complexity(self):
        complexity_score_min, complexity_score_max = m.complexity_score_min_max(
            test_dir)
        self.assertEqual(m.complexity_score('cleaned_1001~Raffi~Wheels-on-the-Bus.txt',
                                            complexity_score_min, complexity_score_max, test_dir), 0.0)


def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFuncOutputs)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    start_time = time.time()
    test_dir = os.getcwd() + '/Testing_Dir'
    main()
#     print("Runtime is:", time.time() - start_time)
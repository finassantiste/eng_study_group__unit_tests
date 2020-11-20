import unittest
from fina.code_challenges.wolf_in_sheeps_clothing.wolf_in_sheeps_clothing import warn_the_sheep


class MyTestWolfCase(unittest.TestCase):

    def test_method_exists(self):
        self.assertTrue(warn_the_sheep())

    #TODO: We forgot to test the parameter! Let's check if warn_the_sheep() takes ina parameter
    # And another test for checking if parameter is list.

    def test_non_list_parameter(self):
        sentence_to_test = "sheep_wolf_queue is not a list"
        self.assertEqual(sentence_to_test, warn_the_sheep())

    def test_returns_pls_go_away_sentence(self):
        sentence_to_test = 'Pls go away and stop eating my sheep'
        #TODO: There's another requirement for this test: if the wolf is the closest animal to you, return ^
        self.assertEqual(sentence_to_test, warn_the_sheep(['sheep', 'sheep', 'wolf']))

    def test_returns_warning_sentence(self):
        sentence1_to_test = 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
        sentence2_to_test = 'Oi! Sheep number 2! You are about to be eaten by a wolf!'
        #TODO: There's another requirement for this test: if the wolf is NOT the closest animal to you, return ^
        self.assertEqual(sentence1_to_test, warn_the_sheep(['sheep', 'sheep', 'wolf', 'sheep']))
        self.assertEqual(sentence2_to_test, warn_the_sheep(['sheep', 'sheep', 'wolf', 'sheep', 'sheep']))



if __name__ == '__main__':
    unittest.main()

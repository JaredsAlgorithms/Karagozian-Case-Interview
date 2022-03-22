"""Test the functionality of the wrapping word search algorithm"""

import unittest
import pathlib

from Algorithms.word_search import WrappingSolution


class WrapTest(unittest.TestCase):
    """
    These unit tests should only test the no wrap functionality
    and will differ results from the other algorithm even on the same data set
    """

    @classmethod
    def setUpClass(cls):
        cls.solution = WrappingSolution(pathlib.Path("inputs/word_search_02.txt"))

    def test_mode(self):
        self.assertTrue(self.solution.mode == "WRAP")

    def test_words(self):
        """Place holder"""
        for word in self.solution.words:
            print(f"[INFO] Checking word: {word}")
            self.solution.exist(word, [])
            # print(self.solution.path)
            self.solution.path.clear()

        # self.assertTrue(self.solution.exist("FED", []))

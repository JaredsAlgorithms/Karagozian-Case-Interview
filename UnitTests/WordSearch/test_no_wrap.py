"""Test the functionality of the no wrapping word search algorithm"""

import unittest
import pathlib

from Algorithms.word_search import NoWrapSolution


class NoWrapTest(unittest.TestCase):
    """
    These unit tests should only test the no wrap functionality
    and will differ results from the other algorithm even on the same data set
    """

    @classmethod
    def setUpClass(cls):
        cls.solution_a = NoWrapSolution(pathlib.Path("inputs/word_search_01.txt"))
        cls.solution_b = NoWrapSolution(pathlib.Path("inputs/word_search_02.txt"))

    def test_mode(self):
        """Make sure we are operating in the correct mode"""
        self.assertTrue(self.solution_a.mode == "NO_WRAP")

    def test_search_word_found(self):
        """The word should be present: FIRST INPUT"""

        self.assertTrue(self.solution_a.exist("FED", []))

        self.assertTrue(self.solution_a.path == [(1, 2), (1, 1), (1, 0)])

        self.solution_a.path.clear()

    def test_search_word_not_found(self):
        """These words should not be present: FIRST INPUT"""

        self.assertTrue(
            not any(
                map(lambda x: self.solution_a.exist(x, []), self.solution_a.words[1:])
            )
        )

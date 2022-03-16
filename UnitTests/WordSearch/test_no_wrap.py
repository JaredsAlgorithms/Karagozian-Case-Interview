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
        cls.solution = NoWrapSolution(pathlib.Path("inputs/word_search_01.txt"))

    def test_search_word_found(self):
        """The word should be present"""

        self.assertTrue(self.solution.exist("FED", []))

        self.assertTrue(self.solution.path == [(1, 0), (1, 1), (1, 2)])

        self.solution.path.clear()

    def test_search_word_not_found(self):
        """These words should not be present"""

        self.assertTrue(
            not any(map(lambda x: self.solution.exist(x, []), self.solution.words[1:]))
        )

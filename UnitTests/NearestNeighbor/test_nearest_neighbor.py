"""Test the functionality of the nearest neighbor algorithm"""

import unittest
import pathlib

from Algorithms.nearest_neighbor import GenericSolution


class NearestNeighborTest(unittest.TestCase):
    """
    These unit tests should only test the no wrap functionality
    and will differ results from the other algorithm even on the same data set
    """

    @classmethod
    def setUpClass(cls):
        cls.solution = GenericSolution(pathlib.Path("inputs/nearest_neighbor.txt"))

        cls.results = [
            [1, 2, 3, 8],
            [0, 4, 6, 8],
            [0, 4, 5, 8],
            [0, 5, 6, 8],
            [1, 2, 7, 8],
            [2, 3, 7, 8],
            [1, 3, 7, 8],
            [4, 5, 6, 8],
            list(range(0, 8)),
        ]

    def test_premade_solutions(self):
        """This should not fail, test solutions given in the requirements"""

        try:
            self.solution.solve(self.results)
        except AssertionError:
            self.fail("[FAILURE] Test should not have failed")

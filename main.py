"""Driver code for all algorithms implemented"""

from Algorithms.word_search import GenericSolution

import pathlib
from pprint import pprint

NoWrapSolution = GenericSolution(pathlib.Path("inputs/word_search_01.txt"))

"""
A B C
D E F
G H I
"""

for word in NoWrapSolution.words:
    if payload := NoWrapSolution.exist(word, []):
        print(NoWrapSolution.path)
        NoWrapSolution.path.clear()

# WrapSolution = GenericSolution(pathlib.Path("inputs/word_search_02.txt"))

# for word in WrapSolution.words:
    # if payload := WrapSolution.exist(word, [(0, len(word)), (len(word), 0), (0, -1 * len(word)), (-1 * len(word), 0)]):
        # print(WrapSolution.path)
        # WrapSolution.path.clear()

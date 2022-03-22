"""Word Search: Programming Challenge 1"""

import typing
import pathlib
import itertools
import types

# Directions we can move

movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1) ,(0, 1), (1, -1), (1, 0), (1, 1)]
# movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class GenericSolution:
    """Encapsulated function to maintain order"""

    def __init__(self, input_: pathlib.Path):
        self.path = []

        with open(input_, "r", encoding="utf-8") as fil_ptr:
            contents = (_.strip() for _ in fil_ptr.readlines())

        self.COL, self.ROW = map(int, next(contents).split(" "))
        self.letters = list(itertools.islice(contents, self.COL))
        # self.letters = map(list, itertools.islice(contents, self.COL))
        print(self.letters)
        self.mode = next(contents)
        self.N = int(next(contents))
        self.words = list(itertools.islice(contents, self.N))

        self._cached_x_domain, self._cached_y_domain = map(
            list, (range(0, self.ROW), range(0, self.COL))
        )


    def out_of_bounds(self, i: int, j: int) -> bool:
        """
        Check if the current pair of indicies are in the confines of the matrix

            Parameters:
                i (int): horizontal position in the matrix
                j (int): vertical position in the matrix
            Returns:
                inside (bool): True if it is inside, False otherwise
        """

        return (
            i < 0
            or i >= self.ROW
            or j < 0
            or j >= self.COL
        )

        # return i not in self._cached_x_domain or j not in self._cached_y_domain

class NoWrapSolution(GenericSolution):
    """Implementation of no wrapping solution"""

    def depth_first_search(
        self,
        i: int,
        j: int,
        word: str,
        position: int,
    ) -> bool:
        """
        Search the grid recursively until we hit a condition where we
        cannot continue processing

        - Horizontal direction under/over flows the grid
        - Vertical direction under/over flows the grid
        - Current grid element does not match the current position in the word

            Parameters:
                i (int): horizontal position in the matrix
                j (int): vertical position in the matrix
                word (str): current word we are searching for
                position (int): position inside the string we are searching for
            Returns:
                exist (bool): conditional return depending on which edge case we're dealig with
        """

        if position == len(word):
            return True

        if self.out_of_bounds(i, j) or self.letters[i][j] != word[position]:
            return False

        for x, y in movements:
            if self.depth_first_search(i + x, j + y, word, position + 1):
                self.path.insert(0, (i, j))
                # self.path.append((i, j))
                return True

        return False

    def exist(self, word: str, extension: typing.List[typing.Tuple[int, int]]):
        """
        Check for it's presence

            Parameters:
                word (str): the word you want to search for
            Returns:
                presence (bool): is in the word search
        """

        movements.extend(extension)

        if len(word) > len(self.letters[0]):
            # Word is too long, no point invoking the algorithm
            print(f"[NOT FOUND]: {word}")
            return False

        for i in range(0, self.ROW):
            for j in range(0, self.COL):
                if self.depth_first_search(i, j, word, 0):
                    print(f"[FOUND]: {word} => {self.path[0]} {self.path[-1]}")
                    return True
        print(f"[NOT FOUND]: {word}")
        return False

class WrappingSolution(GenericSolution):

    def depth_first_search(
        self,
        i: int,
        j: int,
        word: str,
        position: int,
    ) -> bool:
        print(f'i: {i}, j: {j}, position: {position}')
        """
        Search the grid recursively until we hit a condition where we
        cannot continue processing

        - Horizontal direction under/over flows the grid
        - Vertical direction under/over flows the grid
        - Current grid element does not match the current position in the word

            Parameters:
                i (int): horizontal position in the matrix
                j (int): vertical position in the matrix
                word (str): current word we are searching for
                position (int): position inside the string we are searching for
            Returns:
                exist (bool): conditional return depending on which edge case we're dealig with
        """

        if position == len(word):
            # print(position == word[position])
            print(i, j)
            return True

        if not (char := self.get(i, j, position, word)):
            return False
        print(char)
        # if not self.get(i, j):
            # return False

        for x, y in movements:
            if self.depth_first_search(i + x, j + y, word, position + 1):
                self.path.insert(0, (i, j))
                # self.path.append((i, j))
                return True

        return False

    def get(self, i: int, j: int, position: int, word: str) -> bool:
        return types.NoneType if self.out_of_bounds(i, j) else self.letters[i][j] != word[position]

    def exist(self, word: str, extension: typing.List[typing.Tuple[int, int]]):
        """
        Check for it's presence

            Parameters:
                word (str): the word you want to search for
            Returns:
                presence (bool): is in the word search
        """
        for i in range(0, self.ROW):
            for j in range(0, self.COL):
                if self.depth_first_search(i, j, word, 0):
                    # print(f"[FOUND]: {word} => {self.path[0]} {self.path[-1]}")
                    print(f"[FOUND]: {word} => {self.path}")
                    return True
        print(f"[NOT FOUND]: {word}")
        return False

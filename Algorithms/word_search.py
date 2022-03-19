"""Word Search: Programming Challenge 1"""

import typing
import pathlib

# Directions we can move

movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class GenericSolution:
    """Encapsulated function to maintain order"""

    def __init__(self, input_: pathlib.Path):
        self.path = []

        with open(input_, "r", encoding="utf-8") as fil_ptr:
            content = [x.strip() for x in fil_ptr.readlines()]

        # Get the dimensions and convert them into integers

        self.ROW, self.COL = map(int, content[0].split(" "))

        self.letters, self.mode, self.words = (
            list(
                map(list, content[1 : self.COL + 1])
            ),  # get all the characters into a grid
            content[self.COL + 1],
            content[self.COL + 3 :],
        )

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

        return i not in self._cached_x_domain or j not in self._cached_y_domain


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

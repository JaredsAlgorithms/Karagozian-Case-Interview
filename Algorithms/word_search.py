"""Word Search: Programming Challenge 1"""

import typing
import pathlib

# Cardinal direction movements

DX, DY = ((0, 1, 0, -1), (1, 0, -1, 0))

# Combined

movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class GenericSolution:
    """Encapsulated function to maintain order"""

    def __init__(self, input_: pathlib.Path):
        self.path = []

        with open(input_, "r", encoding="utf-8") as fil_ptr:
            content = [x.strip() for x in fil_ptr.readlines()]

        (self.ROW, self.COL), self.letters, self.mode, self.words = (
            list(
                map(int, content[0].split(" "))
            ),  # get the dimensions and convert them into integers
            list(map(list, content[1:4])),  # get all the characters into a grid
            content[4],
            content[6:],
        )
        self.visited = [[False] * self.ROW] * self.COL

    def backtrack(
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
        """

        if position == len(word):
            return True


        if (
            i not in range(0, self.ROW)
            # not i < 0 <= self.ROW
            or j not in range(0, self.COL)
            # or j < 0 <= self.COL
            or self.letters[i][j] != word[position]
            or self.visited[i][j]
        ):
            return False

        self.visited[i][j] = True

        # i < 0 <= self.ROW

        # for x, y in zip(DX, DY):
        for x, y in movements:
            if self.backtrack(i + x, j + y, word, position + 1):
                self.path.append((i, j))
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

        # movements.extend(
        # [(0, len(word)), (len(word), 0), (0, -1 * len(word)), (-1 * len(word), 0)]
        # )

        if len(word) > len(self.letters[0]):
            # Word is too long, no point invoking the algorithm
            return False

        for i in range(0, self.ROW):
            for j in range(0, self.COL):
                if self.backtrack(i, j, word, 0):
                    return True
        return False

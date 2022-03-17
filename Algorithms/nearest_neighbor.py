"""Nearest Neighbor: Programming Challenge 2"""

import ast
import typing
import pathlib
import math


class GenericSolution:
    """Solution for nearest neighbor"""

    def __init__(self, input_: pathlib.Path):
        with open(input_, "r", encoding="utf-8") as fil_ptr:
            content = [x.strip() for x in fil_ptr.readlines()]

        self.radius = float(content[0])
        self.N = int(content[1])
        self.points = list(map(ast.literal_eval, content[2 : 2 + self.N]))

    def solve(self, solutions: typing.List[typing.List[int]]) -> None:
        """
        Time complexity: O(n^2)
            We need to iterate over the current node and all the surrounding nodes
            This means we pass through the list once everytime we loop
            `0` means we have reached ourselves and we need to discard this value
            Therefore, this data set has 9 elements, which means we have at least 81 iterations

        Space complexity: O(n - k)
            `k` denotes the number of nodes that do not conform to the predicate
            This only occurs when we need to print, and I am not sure if you pass a `map` to
            `join` if it creates a temporary list
        """

        assert len(solutions) == self.N

        for solution, (i, point) in zip(solutions, enumerate(self.points)):
            # NOTE: this uses (0, radius] for what is acceptable
            # Constraints stated: (0, radius), however none of the values line up properly

            # O(n - k), where 

            found = [
                i
                for i, neighbor in enumerate(self.points)
                if 0 < math.dist(point, neighbor) <= self.radius
            ]

            # this is dumb because I need to print it with join, takes up O(n) space
            # we could play code golf and turn all the solution lists into lists of strings
            # but I don't feel like doing that

            print(f'{i}: {", ".join(map(str, found))}')

            assert solution == found

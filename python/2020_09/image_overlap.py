"""
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary 
matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of 
units), and place it on top of the other image.  After, the overlap of this translation is the 
number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?


https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3450/
"""
import numpy as np


class Solution:
    def largestOverlap(self, A: list, B: list) -> int:
        max_match = 0
        # Handle empty
        # Handle Same
        max_match = max(max_match, self.check(A, B))
        for _i in range(len(A)-1):
            # shift vertical
            B = np.roll(B, -1, axis=0)
            # Check pre horizontal shift
            max_match = max(max_match, self.check(A, B))
            for _j in range(len(A[0])-1):
                # shift horizontal
                B = np.roll(B, -1, axis=1)
                # check after horizontal shift
                max_match = max(max_match, self.check(A, B))
        return max_match

    def check(self, A, B):
        # and
        matrix_and = np.bitwise_and(A, B)
        # condense columns
        condense_1 = sum(matrix_and)
        condense_2 = sum(condense_1)
        print(f"Got a total of {condense_2} for:\n\tA: {A}\n\tB:{B}")
        return condense_2


def test_1():
    given = {
        "A": [[1, 1, 0],
              [0, 1, 0],
              [0, 1, 0]],
        "B": [[0, 0, 0],
              [0, 1, 1],
              [0, 0, 1]]
    }
    expected = 3
    assert Solution().largestOverlap(**given) == expected


def test_2():
    given = {
        "A": [[0, 1],
              [1, 1]],
        "B": [[1, 1],
              [1, 0]]
    }
    expected = 2
    assert Solution().largestOverlap(**given) == expected


def test_3():
    given = {
        "A": [[1, 1, 1],
              [1, 0, 0],
              [0, 1, 1]],
        "B": [[1, 1, 0],
              [1, 1, 1],
              [1, 1, 0]]
    }
    expected = 4
    assert Solution().largestOverlap(**given) == expected

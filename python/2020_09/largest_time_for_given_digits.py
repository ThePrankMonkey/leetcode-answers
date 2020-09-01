"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.
Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/
"""

from itertools import permutations
import re


def largestTimeFromDigits(A: list) -> str:
    # Get a set of all possible permutations, in decreasing order
    candidates = sorted(["".join([str(i) for i in t])
                         for t in set(permutations(A))], reverse=True)
    # Find the first that matches valid time string format
    r_string = r"(([0-1][0-9])|(2[0-3]))[0-5][0-9]"
    for candidate in candidates:
        if re.match(r_string, candidate):
            # Add the ":"
            return f"{candidate[:2]}:{candidate[2:]}"
    return ""


def test_1():
    given = [1, 2, 3, 4]
    expect = "23:41"
    assert largestTimeFromDigits(given) == expect


def test_2():
    given = [5, 5, 5, 5]
    expect = ""
    assert largestTimeFromDigits(given) == expect

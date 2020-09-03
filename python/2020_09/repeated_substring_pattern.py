"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447/

Solution Thoughts:
If the I rotate the string one char at a time and it is ever the same string, it must be made of repeated segments.

Time Complexity:
    O(2n) due to the for loop and comparison.
    
Space Complexity:
    Sigma(1) for the single new string being created.
"""


def repeatedSubstringPattern(s: str) -> bool:
    # rotate string and compare
    new_s = s[:]
    # print(f"{s}")
    for _ in range(len(s)//2):
        new_s = f"{new_s[-1]}{new_s[:-1]}"
        # print(f"\t{new_s}")
        if new_s == s:
            return True
    return False


def test_1():
    given = "abab"
    expected = True
    assert repeatedSubstringPattern(given) == expected


def test_2():
    given = "aba"
    expected = False
    assert repeatedSubstringPattern(given) == expected


def test_3():
    given = "abcabcabcabc"
    expected = True
    assert repeatedSubstringPattern(given) == expected

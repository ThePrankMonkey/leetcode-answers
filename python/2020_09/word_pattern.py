"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in str.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/

"""


class Solution:
    def wordPattern(self, pattern: str, phrase: str) -> bool:
        letters = list(dict.fromkeys(pattern))
        # print(letters)
        word_dict = {}
        found_pattern = []
        words = phrase.split()
        # print(words)
        try:
            for word in words:
                if word not in word_dict:
                    word_dict[word] = letters.pop(0)
                found_pattern.append(word_dict[word])
            # print(found_pattern)
            return pattern == "".join(found_pattern)
        except IndexError:
            return False


def test_1():
    given = {
        "pattern": "abba",
        "phrase": "dog cat cat dog"
    }
    expected = True
    assert Solution().wordPattern(**given) == expected


def test_2():
    given = {
        "pattern": "abba",
        "phrase": "dog cat cat fish"
    }
    expected = False
    assert Solution().wordPattern(**given) == expected


def test_3():
    given = {
        "pattern": "aaaa",
        "phrase": "dog cat cat dog"
    }
    expected = False
    assert Solution().wordPattern(**given) == expected


def test_4():
    given = {
        "pattern": "abba",
        "phrase": "dog dog dog dog"
    }
    expected = False
    assert Solution().wordPattern(**given) == expected

"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in str.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/

Solution Thoughts:
First, get an ordered set from the pattern. Python 3.6 lets you preserve order in a dict so we can use that.
  This is so I can prevent duplicates.
Second, for each word in the phrase either find what letter it has or give it the next letter in our set.
  Track these letters.
Third, compare original pattern to tracked letters.
Optimization comes from joining a list of tracked letters as that is far faster than remaking a string.

Time Complexity:
n is length of pattern
m is count of words in phrase
l is length of phrase
O(2n+3m+l)
  2n from making a dict and then a list from each letter in the pattern. It'll often be faster as 
    the second half probably has duplicate letters removed.
  l is from spliting the phrase (it has to check for each char if a space).
  3m is from the O(n) for loop over the words, the O(1) check or assignment for each one, 
    and the O(n) join for each letter found.

Space Complexity:
n is length of pattern
m is count of words in phrase
O(2n+m)
  2n is from a duplicate list of letters and tracked letters
  m is the list of words we get from splitting the phrase.
"""


class Solution:
    def wordPattern(self, pattern: str, phrase: str) -> bool:
        # Get an "ordered" set
        letters = list(dict.fromkeys(pattern))
        word_dict = {}
        found_pattern = []
        words = phrase.split()
        try:
            for word in words:
                # check if the word has been encountered or assign it the next letter
                if word not in word_dict:
                    word_dict[word] = letters.pop(0)
                # grab the letter for that word
                found_pattern.append(word_dict[word])
            return pattern == "".join(found_pattern)
        except IndexError:  # if we run out of letters we must have failed.
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

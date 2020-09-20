"""
You are playing the following Bulls and Cows game with your friend: 
You write down a number and ask your friend to guess what the number 
is. Each time your friend makes a guess, you provide a hint that 
indicates how many digits in said guess match your secret number 
exactly in both digit and position (called "bulls") and how many 
digits match the secret number but locate in the wrong position 
(called "cows"). Your friend will use successive guesses and hints to 
eventually derive the secret number.

Write a function to return a hint according to the secret number and 
friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain 
duplicate digits.


https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3455/

Solution Thoughts:

Time Complexity:
O(n). n from making the counter, another n from the for loop, and two 
  more n to sum up the counters that dipped below zero. 4n => n

Space Complexity:
O(n). n from the counter, 1 for each cows and bulls, and another n
  for the summation comprehension. 2n + 2 => n.
"""

from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_counts = Counter(secret)
        print(f"{secret_counts=}")
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                secret_counts.subtract(guess[i])
                # print(f"Found bull: {i=} {guess[i]}")
            else:
                if guess[i] in secret_counts:
                    cows += 1
                    secret_counts.subtract(guess[i])
                    # print(f"Found cow:  {i=} {guess[i]}")
                    # print(f"{secret_counts=}")
        cows += sum([i for i in secret_counts.values() if i < 0])
        return f"{bulls}A{cows}B"


def test_1():
    given = {"secret": "1807", "guess": "7810"}
    expected = "1A3B"
    assert Solution().getHint(**given) == expected


def test_2():
    given = {"secret": "1123", "guess": "0111"}
    expected = "1A1B"
    assert Solution().getHint(**given) == expected

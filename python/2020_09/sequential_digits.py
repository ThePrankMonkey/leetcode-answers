"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/

Solution Thoughts:
Initially, I thought of just iterating over every value between low and high, and checking if they were sequential, but that sounded slow.
Then I thought of just making every sequential value between low and high. My first attempt follows where I use strings to build the numbers.
    String casting was used because it's incredibly fast. Even faster than logarithmic math.
    https://stackoverflow.com/questions/33947632/get-most-significant-digit-in-python/33947673

Complexity:

Time: O(1)
    There are a finite number of possible sequential strings in any range, so this is essentially constant time.
Space: O(1)
    I'm only working on a single string at a time, and tracking a couple numbers.
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        for i in range(1, 10):
            num = f"{i}"
            cur_num = i
            while int(num) < high:
                cur_num += 1
                if cur_num == 10:
                    # print("Breaking at 10")
                    break
                num += str(cur_num)
                # print(f"{num=}")
                if low <= int(num) <= high:
                    results.append(int(num))
        return sorted(results)


def test_1():
    given = {
        "low": 100,
        "high": 300
    }
    expected = [123, 234]
    assert Solution().sequentialDigits(**given) == expected


def test_2():
    given = {
        "low": 1000,
        "high": 13000
    }
    expected = [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    assert Solution().sequentialDigits(**given) == expected

"""
Given a list of non negative integers, arrange them such that they form the largest number.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472/

Time Complexity: O(nlog(n))
We have O(n) from the list comprehension, no real way to skip that as we need to remap the values from ints.
  map() is discouraged in pep guidance. It's a lot easier to see what is being done. Technically 
  nums = map(str, nums) is a little faster, but not enough to lose clarity in code.
We then have to sort these strings, Bubble Sort does it in O(nlog(n)). But we can speed it up by a decent
  amount by using the built in timsort. Still, worst case is O(nlog(n)). To make a key for timsort, we 
  need to use a comparator. Python3 dropped support in sort() for cmp, so we need to use the built in 
  functools.cmp_to_key(). To the best of my knowledge, there's no better way to do this out of manually
  remaking timsort from scratch.
The comparator function will take the let sort() know to swap if the a+b is less than b+a.

Space Complexity: O(n)
We replace the list, and then re sort in place.
"""

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list) -> str:
        # list comprehension to make into strings, preffered over map()
        nums = [str(n) for n in nums]

        # bubble sort
        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-i-1):
        #         if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]

        # Comparator function
        def f(a, b):
            if a+b < b+a:
                return -1
            return 0
        # use timsort which is often faster than bubble sort
        nums.sort(key=cmp_to_key(f), reverse=True)
        # chance of weird edge cases like "0000", so evaluates back down to "0"
        return str(int("".join(nums)))


def test_1():
    given = {
        "nums": [10, 2],
    }
    expected = "210"
    assert Solution().largestNumber(**given) == expected


def test_2():
    given = {
        "nums": [3, 30, 34, 5, 9],
    }
    expected = "9534330"
    assert Solution().largestNumber(**given) == expected

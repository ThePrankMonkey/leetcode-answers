"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

import sys
class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum = max_cur = -1*sys.maxsize
        for i in range(len(nums)):
            max_cur = max(nums[i], max_cur + nums[i])
            max_sum = max(max_sum, max_cur)
        return max_sum

def test_1():
    given = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    solution = Solution()
    assert solution.maxSubArray(given) == expected

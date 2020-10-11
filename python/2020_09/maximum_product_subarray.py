"""

"""

import sys


class Solution:
    def maxProduct(self, nums: list) -> int:
        print(nums)
        if len(nums) == 1:
            return nums[0]
        max_so_far = -sys.maxsize - 1
        for i, num1 in enumerate(nums[:-1]):
            max_so_far = max(max_so_far, num1)
            for num2 in nums[i+1:]:
                num1 *= num2
                max_so_far = max(max_so_far, num1)
        max_so_far = max(max_so_far, nums[-1])
        return max_so_far


def test_1():
    given = {"nums": [2, 3, -2, 4]}
    expected = 6
    assert Solution().maxProduct(**given) == expected


def test_2():
    given = {"nums": [-2, 0, -1]}
    expected = 0
    assert Solution().maxProduct(**given) == expected

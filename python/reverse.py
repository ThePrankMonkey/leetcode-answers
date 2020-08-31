"""
https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        multiply = 1
        upper_bound = 2**31-1
        lower_bound = -2**31
        if x < 0:
            multiply = -1
        value = int(str(abs(x))[::-1])
        print(f"mult={multiply}, value={value}, final={multiply*value}")
        if lower_bound < value < upper_bound:
            # prin(f"{lower_bound} < {value} < {upper_bound}")
            return multiply * value
        return 0


def test_1():
    assert Solution().reverse(-123) == -321

def test_outOfScope():
    assert Solution().reverse(1534236469) == 0
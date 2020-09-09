"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1;
if version1 < version2 return -1;
otherwise return 0.

You may assume that the version strings are non-empty and contain only digits 
and the . character.

The . character does not represent a decimal point and is used to separate 
number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it 
is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number 
to be 0. For example, version number 3.4 has a revision number of 3 and 4 for 
its first and second level revision number. Its third and fourth level 
revision number are both 0.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3454/

Solution Thoughts:
1. Split up the strings into parts. That's an O(n) operation as I am parsing 
   the string.
2. Pick one that is longer and set it as the one driving the loop. O(1) for 
   each as the objects track their length. Track if order is switched.
3. Loop over this one. Will be max(O(a), O(b))
4. Check if the value is equal or higher. Lower can be logically derived from 
   those.
   4a. Assume value of 0 if absent.
5. Return result.

Time Complexity:
O(a+b+max(a,b))

Space Complexity:
O(a+b)

Optimization:
I can probably reduce space complexity to O(1) with the use of generators in 
place of using the split. And then just popping off the next chunk instead 
of grabbing an index.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts_1 = self.get_value(version1)
        parts_2 = self.get_value(version2)
        if len(parts_1) > len(parts_2):
            looper = parts_1
            follow = parts_2
            multiplier = 1
        else:
            looper = parts_2
            follow = parts_1
            multiplier = -1
        for i in range(len(looper)):
            try:
                check_equal = looper[i] == follow[i]
                check_great = looper[i] > follow[i]
            except IndexError:
                check_equal = looper[i] == 0
                check_great = looper[i] > 0
            if not check_equal:
                if check_great:
                    return 1 * multiplier
                return -1 * multiplier
        return 0

    def get_value(self, value):
        parts = [int(x) for x in value.split(".")]
        return parts


def test_1():
    given = {
        "version1": "0.1", "version2": "1.1"
    }
    expected = -1
    assert Solution().compareVersion(**given) == expected


def test_2():
    given = {
        "version1": "1.0.1", "version2": "1"
    }
    expected = 1
    assert Solution().compareVersion(**given) == expected


def test_3():
    given = {
        "version1": "7.5.2.4", "version2": "7.5.3"
    }
    expected = -1
    assert Solution().compareVersion(**given) == expected


def test_4():
    given = {
        "version1": "1.01", "version2": "1.001"
    }
    expected = 0
    assert Solution().compareVersion(**given) == expected


def test_5():
    given = {
        "version1": "1.0", "version2": "1.0.0"
    }
    expected = 0
    assert Solution().compareVersion(**given) == expected

"""
There are some spherical balloons spread in two-dimensional space. For each balloon, 
provided input is the start and end coordinates of the horizontal diameter. Since 
it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start 
and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. A 
balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
There is no limit to the number of arrows that can be shot. An arrow once shot keeps 
traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of 
arrows that must be shot to burst all balloons.

Constraints:

    0 <= points.length <= 104
    points.length == 2
    -231 <= xstart < xend <= 231 - 1


https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3490/

Time Complexity: O(nlog(n))
  O(nlog(n)) from the sort to align right edges.
  O(n) from going over the list.
  O(nlog(n)) + O(n) = O(nlog(n))
Space Complexity: O(1)
  List is sorted in place, and only two integers (current edge, and count of 
    arrows) are used to track information.
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Handle edge case with not balloons
        if not points:
            return 0
        # Sort to align right edge of balloons
        points.sort(key=lambda x: x[1])
        arrows = 1
        edge = points[0][1]
        for point in points:
            # If balloon is going to be hit, skip it
            if point[0] <= edge:
                continue
            # Else the balloon would be missed, so new arrow and new edge.
            arrows += 1
            edge = point[1]
        return arrows


def test_1():
    given = {
        "points": [[10, 16], [2, 8], [1, 6], [7, 12]],
    }
    expected = 2
    assert Solution().findMinArrowShots(**given) == expected


def test_2():
    given = {
        "points": [[1, 2], [3, 4], [5, 6], [7, 8]],
    }
    expected = 4
    assert Solution().findMinArrowShots(**given) == expected


def test_3():
    given = {
        "points": [[1, 2], [2, 3], [3, 4], [4, 5]],
    }
    expected = 2
    assert Solution().findMinArrowShots(**given) == expected


def test_4():
    given = {
        "points": [[1, 2]],
    }
    expected = 1
    assert Solution().findMinArrowShots(**given) == expected


def test_5():
    given = {
        "points": [[2, 3], [2, 3]],
    }
    expected = 1
    assert Solution().findMinArrowShots(**given) == expected

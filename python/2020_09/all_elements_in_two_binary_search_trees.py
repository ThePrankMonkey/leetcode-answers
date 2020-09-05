"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3449/

Solution Thoughts:

1. Perform an in-order search (left, val, right) to make two lists that are already ordered.
   This will simplify the work to sort them together.
2. Combine the two lists and sort those. Might be more efficient ways to zipper them.

Time Complexity:
O(2(n+m)). n for first tree getting traversed, m for second tree getting traversed.
  Sorted() is nlog(n) normally, but since they are presorted, it's actually n+m.

Space Complexity:
O(n+m). I make two lists of n and m length, and then combine and sort in place.

"""


class TreeNode:
    """
    Predefined tree class.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Predefined solution class.
    """

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Actual solution method.
        """
        list1 = []
        list2 = []
        self.traverse(root1, list1)
        self.traverse(root2, list2)
        results = sorted(list1 + list2)
        return results

    def traverse(self, node, list_to_add):
        """
        Traversed tree in pre-sort order.
        """
        if not node:
            return
        if node.left:
            self.traverse(node.left, list_to_add)
        list_to_add.append(node.val)
        if node.right:
            self.traverse(node.right, list_to_add)

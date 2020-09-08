"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.


https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/


"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total_of_paths = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.traverse_and_track(root)
        return self.total_of_paths

    def traverse_and_track(self, node, current=""):
        current += str(node.val)
        if not node.left and not node.right:
            new_number = int(f"0b{current}", 2)
            print(f"{current} => {new_number}")
            self.total_of_paths += new_number
        if node.left:
            self.traverse_and_track(node.left, current)
        if node.right:
            self.traverse_and_track(node.right, current)


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    assert Solution().sumRootToLeaf(root) == 22

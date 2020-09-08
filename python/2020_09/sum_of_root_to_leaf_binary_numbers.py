"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.


https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/


"""


# class TreeNode:
#     # Definition for a binary tree node.
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     def insert(self, num):
#         if self.val:
#             if num == 0:
#                 if self.left is None:
#                     print(f"Creating a node for {num}")
#                     self.left = TreeNode(num)
#                 else:
#                     self.left.insert(num)
#             elif num == 1:
#                 if self.right is None:
#                     print(f"Creating a node for {num}")
#                     self.right = TreeNode(num)
#                 else:
#                     self.right.insert(num)
#             else:
#                 print("Something is broken")
#         else:
#             print(f"Setting a node to {num}")
#             self.val = num


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


# def test_1():
#     insertions = [1, 0, 1, 0, 1, 0, 1]
#     root = TreeNode()
#     for num in insertions:
#         print(f"Insertion {num}")
#         root.insert(num)
#     assert Solution().sumRootToLeaf(root) == 22

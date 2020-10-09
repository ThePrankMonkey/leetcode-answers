"""

Serialization is converting a data structure or object into a sequence of bits so 
that it can be stored in a file or memory buffer, or transmitted across a network 
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no 
restriction on how your serialization/deserialization algorithm should work. You need 
to ensure that a binary search tree can be serialized to a string, and this string 
can be deserialized to the original tree structure.

The encoded string should be as compact as possible.


https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3489/

Time Complexity: 
Serialize = O(n)
  We only traverse each node once.
Deserialize = O(nlog(n))
  We keep recursively start from root node and will hit nodes over and over again while 
  finding where to place the newest node.

Space Complexity: O(n)
We only ever have to deal with an array or the tree, and they are equal size to the input.
"""

import json  # Simple serialization/deserialization of lists.


class TreeNode:
    """Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """Solution
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.arr = []
        self.__traverse(root)
        result = json.dumps(self.arr)
        # print(f"Serialized: {result}")
        return result

    def __traverse(self, node: TreeNode):
        """Preorder Traversal
        """
        if node:
            self.arr.append(node.val)
            self.__traverse(node.left)
            self.__traverse(node.right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = json.loads(data)
        if arr:
            # Create the root node to insert into
            root = TreeNode(arr[0])
        else:
            # Break if data string is empty
            return []
        for num in arr[1:]:
            self.__insert(root, num)
        return root

    def __insert(self, node: TreeNode, data: int):
        """Binary Insertion
        """
        if data >= node.val:
            if node.right:
                self.__insert(node.right, data)
            else:
                node.right = TreeNode(data)
        else:
            if node.left:
                self.__insert(node.left, data)
            else:
                node.left = TreeNode(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

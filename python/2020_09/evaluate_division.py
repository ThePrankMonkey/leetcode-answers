"""
You are given equations in the format A / B = k, where A and B are variables represented as 
strings, and k is a real number (floating-point number). Given some queries, return the answers. 
If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division 
by zero and there is no contradiction.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3474/


"""

from collections import defaultdict, deque


class Graph():
    def __init__(self, paths, values):
        self.graph = defaultdict(list)
        for (start, end), value in zip(paths, values):
            # Add forwards
            self.__add_edge(start, end, value)
            # Add backwards
            self.__add_edge(end, start, 1/value)

    def __add_edge(self, start, end, value):
        self.graph[start].append((end, value))

    def find_path(self, query):
        start, end = query
        if start not in self.graph or end not in self.graph:
            return -1.0
        queue = deque([(start, 1.0)])
        visited = set()
        while queue:
            front, cur_product = queue.popleft()
            if front == end:
                return cur_product
            visited.add(front)
            for neighbor, value in self.graph[front]:
                if neighbor not in visited:
                    queue.append((neighbor, cur_product*value))
        return -1.0


class Solution:
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        graph = Graph(equations, values)
        return [graph.find_path(q) for q in queries]


def test_1():
    given = {
        "equations": [["a", "b"], ["b", "c"]],
        "values": [2.0, 3.0],
        "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    }
    expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    assert Solution().calcEquation(**given) == expected


def test_2():
    given = {
        "equations": [["a", "b"], ["b", "c"], ["bc", "cd"]],
        "values": [1.5, 2.5, 5.0],
        "queries": [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    }
    expected = [3.75000, 0.40000, 5.00000, 0.20000]
    assert Solution().calcEquation(**given) == expected


def test_3():
    given = {
        "equations": [["a", "b"]],
        "values": [0.5],
        "queries": [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    }
    expected = [0.50000, 2.00000, -1.00000, -1.00000]
    assert Solution().calcEquation(**given) == expected

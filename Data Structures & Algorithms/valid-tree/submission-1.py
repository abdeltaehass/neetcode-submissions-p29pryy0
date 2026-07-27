from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes must have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [1] * n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node

        def union(node1: int, node2: int) -> bool:
            root1 = find(node1)
            root2 = find(node2)

            # A shared root means this edge creates a cycle.
            if root1 == root2:
                return False

            # Union by rank.
            if rank[root1] < rank[root2]:
                root1, root2 = root2, root1

            parent[root2] = root1
            rank[root1] += rank[root2]

            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return False

        return True
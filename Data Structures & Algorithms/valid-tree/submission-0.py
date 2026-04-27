class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # شرط لازم: تعداد یال‌ها باید n-1 باشد
        if len(edges) != n - 1:
            return False

        # ساخت adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        # چک اتصال
        return dfs(0, -1) and len(visit) == n
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            res = time

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + weight, nei))

        return res if len(visited) == n else -1
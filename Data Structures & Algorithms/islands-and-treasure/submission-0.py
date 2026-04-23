class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        grid[nr][nc] == -1 or
                        (nr, nc) in visit
                    ):
                        continue

                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1
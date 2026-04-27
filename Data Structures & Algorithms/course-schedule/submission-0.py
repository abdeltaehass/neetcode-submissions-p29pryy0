class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if prevMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            prevMap[crs] = []  # mark as completed
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
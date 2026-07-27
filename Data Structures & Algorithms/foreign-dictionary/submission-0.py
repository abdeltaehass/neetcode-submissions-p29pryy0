from typing import List
from collections import defaultdict


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}

        # Build the graph.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Invalid case:
            # ["abc", "ab"]
            if (
                len(word1) > len(word2)
                and word1.startswith(word2)
            ):
                return ""

            min_length = min(len(word1), len(word2))

            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visited = {}  # False = visiting, True = visited
        order = []

        def dfs(char: str) -> bool:
            if char in visited:
                return visited[char]

            visited[char] = False

            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False

            visited[char] = True
            order.append(char)

            return True

        for char in graph:
            if not dfs(char):
                return ""

        order.reverse()
        return "".join(order)
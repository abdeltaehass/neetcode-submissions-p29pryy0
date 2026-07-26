from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build the Trie.
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row: int, col: int, parent: TrieNode) -> None:
            char = board[row][col]

            if char not in parent.children:
                return

            node = parent.children[char]

            # We found a complete word.
            if node.word is not None:
                result.append(node.word)
                node.word = None  # Prevent duplicate results.

            # Mark this cell as visited.
            board[row][col] = "#"

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ]

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] != "#"
                ):
                    dfs(new_row, new_col, node)

            # Restore the cell for other searches.
            board[row][col] = char

            # Remove dead Trie branches to improve performance.
            if not node.children and node.word is None:
                del parent.children[char]

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.word

            c = word[i]
            if c == ".":
                return any(dfs(i + 1, child) for child in node.children.values())

            if c not in node.children:
                return False
            return dfs(i + 1, node.children[c])

        return dfs(0, self.root)

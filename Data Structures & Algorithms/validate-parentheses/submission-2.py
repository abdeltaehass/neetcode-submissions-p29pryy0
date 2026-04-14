class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for p in s:
            if p in pairs:
                if stack and stack[-1] == pairs[p]:
                    stack.pop()
                else: return False
            else: stack.append(p)
        return True if not stack else False
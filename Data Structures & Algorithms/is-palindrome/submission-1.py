class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = "".join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()
        reversed_s = cleaned[::-1]

        for c in range(len(cleaned)):
            if reversed_s[c] != cleaned[c]:
                return False
        return True

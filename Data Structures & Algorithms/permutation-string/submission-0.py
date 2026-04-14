class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need, window = [0] * 26, [0] * 26
    
        for c in s1:
            need[ord(c) - ord('a')] += 1
        
        k = len(s1)

        for i in range(k):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True
        
        for i in range(k, len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - k]) - ord('a')] -= 1

            if window == need:
                return True
        return False
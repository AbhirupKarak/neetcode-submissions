class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1Count = [0] * 26
        s2Count = [0] * 26
        left = 0
        if len(s2) < len(s1):
            return False
        for char in s1:
            s1Count[ord(char) - ord('a')] += 1
        for i in range(0, k):
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        if s2Count == s1Count:
                return True
        
        for right in range(k, len(s2)):
            s2Count[ord(s2[right]) - ord('a')] += 1
            s2Count[ord(s2[left]) - ord('a')] -= 1
            left += 1
            if s2Count == s1Count:
                return True
        return False





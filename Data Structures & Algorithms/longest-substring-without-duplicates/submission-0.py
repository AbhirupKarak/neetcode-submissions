class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxLen = 0
        for right, char in enumerate(s):#expanding if unique, shrinking if duplicate
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            right += 1
            maxLen = max(maxLen, right - left)
        return maxLen
        

        
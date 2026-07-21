class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLen = len(s)
        need = {}
        windowCount = {}
        matches = 0 
        resLeft = 0
        resRight = 0
        resLen = float('inf')

        if not s and not t:
            return ""

        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        right = 0
        for right in range(len(s)):
            windowCount[s[right]] = windowCount.get(s[right], 0) + 1
            if s[right] in need and windowCount[s[right]] == need[s[right]]:
                matches += 1

            while (matches == len(need)):
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    resLeft, resRight = left, right
                leftChar = s[left]
                if leftChar in need and windowCount[leftChar] == need[leftChar]:
                    matches -= 1
                windowCount[leftChar] -= 1
                left += 1
        
        if resLen == float('inf'):
            return ""
        return s[resLeft:resRight + 1]
        

            

        
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        windowCount = {}
        matches = 0
        resLen = float("inf")
        resleft, resRight = 0, 0

        if not s and not t:
            return ""
        
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        right = 0

        for right in range(len(s)):
            char =  s[right]
            windowCount[char] = windowCount.get(char, 0) + 1
            if char in need and windowCount[char] == need[char]:
                matches += 1

            while (len(need) == matches):
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    resLeft, resRight = left, right
                leftChar = s[left]
                if leftChar in need and windowCount[leftChar] == need[leftChar]:
                    matches -= 1
                windowCount[leftChar] -= 1
                left += 1
        
        if resLen == float("inf"):
            return ""
        
        return s[resLeft:resRight + 1]





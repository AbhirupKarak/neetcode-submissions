class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)
        for num in numSet:
            if (num - 1) not in numSet:
                current = num
                length = 1
                while (current + 1) in numSet:
                    current += 1
                    length += 1
                maxLen = max(length, maxLen)
        return maxLen
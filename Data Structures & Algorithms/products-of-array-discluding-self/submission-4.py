class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: #Brute Force + prefix_suffix_array
        res = []
        prefixArray = [1]*len(nums)
        suffixArray = [1]*len(nums)
        for i in range(1, len(nums)):
            prefixArray[i] = prefixArray[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffixArray[i] = suffixArray[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            res.append(prefixArray[i]*suffixArray[i])

        return res


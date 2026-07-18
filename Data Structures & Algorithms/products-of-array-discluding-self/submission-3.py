class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: #Brute Force
        res = []
        prefixArray = []
        suffixArray = []
        for i in range(len(nums)):
            product = 1
            for j in range(0,i):
                product *= nums[j]
            prefixArray.append(product)

        for i in range(len(nums)):
            product = 1
            for j in range(i + 1, len(nums)):
                product *= nums[j]
            suffixArray.append(product)
        for i in range(len(nums)):
            res.append(prefixArray[i]*suffixArray[i])
            
        return res


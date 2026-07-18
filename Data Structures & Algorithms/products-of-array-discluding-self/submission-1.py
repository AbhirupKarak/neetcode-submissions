class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        pointer = 0 
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if (j != pointer):
                    product *= nums[j]
            pointer += 1
            res.append(product)
            product = 1
        return res


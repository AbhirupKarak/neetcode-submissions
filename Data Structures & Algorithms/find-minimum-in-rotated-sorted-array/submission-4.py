class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        first we find this cut in the array.
        if the cut i.e. the largest element lands on the last index then
        it is the original array itself
        else. 
        if the cut is anywhere else. the element on the next index is the smallest element.
        condition to check: binary search to check if arr[i] < arr[i-1]
        '''

        cut = 0
        l = 0
        r = len(nums) - 1
        mid = (l + r)// 2
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        
        while(l <= r):
            mid = (l + r)// 2
            if mid and nums[mid] < nums[mid - 1]:
                #cut is found
                return nums[mid]
            elif nums[mid] < nums[-1]: #mid and r are in same sorted segment
                r = mid - 1
            else: #l and mid are in same sorted segment
                l = mid + 1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        lets break the array into two sorted arrays
        for eg 
        [3,4,5,6,1,2]
        can be thought of as 
        [3,4,5,6] and [1,2]
        without breaking the array or creating a new one
        we look for the cut
        and run two separate binary searches in the two sublists
        '''

        l = 0
        r = len(nums) - 1
        cut_idx = 0
        # first we find the cut
        while(l <= r):
            mid = (l + r) // 2
            if mid and nums[mid] < nums[mid - 1]:
                cut_idx = mid
                break
            elif nums[mid] < nums[-1]:
                r = mid - 1
            else:
                l = mid + 1
        #cut index found
        print(cut_idx)

        l1 = 0
        r1 = cut_idx - 1
        l2 = cut_idx 
        r2 = len(nums) - 1

        while(l1 <= r1):
            mid1 = (l1 + r1) // 2
            if nums[mid1] == target:
                return mid1
            elif nums[mid1] < target:
                l1 = mid1 + 1
            else:
                r1 = mid1 - 1
        
        while (l2 <= r2):
            mid2 = (l2 + r2) // 2
            if nums[mid2] == target:
                return mid2
            elif nums[mid2] < target:
                l2 = mid2 + 1
            else:
                r2 = mid2 - 1
        return -1
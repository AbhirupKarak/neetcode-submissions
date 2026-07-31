class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        #im declaring nums1 < nums2
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2
        # we run binary search to find the correct left partition
        # we run it on the smaller array
        l = 0
        r = m 
        while(l <= r):
            mid = (l + r) // 2
            #here we compute the left partition for the bigger array by using 
            #half - (mid + 1)
            l_part = half - mid     #length of left part. in bigger array
            left1 = float("-inf") if mid == 0 else nums1[mid - 1]
            right1 = float("inf") if mid == m else nums1[mid]

            left2 = float("-inf") if l_part == 0 else nums2[l_part - 1]
            right2 = float("inf") if l_part == n else nums2[l_part]

            if left1 <= right2 and left2 <= right1:
                #partition is valid
                if (m + n) % 2 == 1: #odd
                    return max(left1, left2)
                else:
                    return float((max(left1,left2) + min(right1, right2))/2)
            elif left2 <= right1 and left1 > right2:
                #case where left partition of smaller array must be made smaller because
                #of above condition
                r = mid - 1
            else:
                l = mid + 1
        return 0.0

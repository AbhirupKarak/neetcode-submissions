class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0, 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow2 = 0
        while(slow != slow2):
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow
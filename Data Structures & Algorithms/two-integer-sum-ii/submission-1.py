class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while(left != len(numbers) - 1 and right != 0):
            twoSum = numbers[left] + numbers[right]
            if (twoSum == target):
                return [left + 1, right + 1]
            elif (twoSum < target):
                left += 1
            else:
                right -= 1
            
        
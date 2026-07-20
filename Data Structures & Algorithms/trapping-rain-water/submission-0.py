class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMaxArr = [0] * n
        rightMaxArr = [0] * n
        leftMaxArr[0] = height[0]
        rightMaxArr[n - 1] = height[n - 1]

        for i in range(1, n):
            leftMaxArr[i] = max(leftMaxArr[i-1], height[i])
        
        for i in range(n - 2, -1, -1):
            rightMaxArr[i] = max(rightMaxArr[i + 1], height[i])
        
        totalArea = 0

        for i, h in enumerate(height):
            if (min(leftMaxArr[i], rightMaxArr[i]) > h):
                area = min(leftMaxArr[i], rightMaxArr[i]) - h
                totalArea += area
        return totalArea

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = []
        if len(heights) == 1:
            return heights[0]
        for i in range(len(heights)):
            while st and heights[i] < heights[st[-1]]:
                x = st.pop()
                if not st:
                    currArea = heights[x] * (i)
                else:
                    currArea = heights[x] * (i - st[-1] - 1)
                maxArea = max(maxArea, currArea)
            st.append(i)
        while st:
            x = st.pop()
            if st:
                currArea = heights[x] * (len(heights) - st[-1] - 1)
            else:
                currArea = heights[x] * (len(heights))
            maxArea = max(maxArea, currArea)

        return maxArea
        
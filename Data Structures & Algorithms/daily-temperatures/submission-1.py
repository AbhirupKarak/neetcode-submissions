class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        
        for i, temp in enumerate(temperatures):
            while st and temp > temperatures[st[-1]]:
                j = st.pop()
                res[j] = i - j
            st.append(i)
    
        return res
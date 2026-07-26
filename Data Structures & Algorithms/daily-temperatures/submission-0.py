class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = tuple(temperatures)
        res = []
        for i in range(len(temps)):
            for j in range(i + 1, len(temps)):
                if (temps[j] <= temps[i]) and j == len(temps) - 1:
                    res.append(0) 
                elif(temps[j] < temps[i]):
                    continue
                elif (temps[j] > temps[i]):
                    res.append(j - i)
                    break
            if i == len(temps) - 1:
                res.append(0)
        return res


            
                
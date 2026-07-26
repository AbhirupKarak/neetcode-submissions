class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeTkn = []
        for i, pos in enumerate(position):#calculating time taken by each car to reach target
            timeTkn.append((target-pos)/speed[i])

        #sorting each car in descending order based on their distance from target
        cars = list(zip(position, timeTkn))
        cars.sort(reverse = True)

        maxTime = 0
        fleets = 0
        for pos, time in cars:
            if maxTime < time:
                fleets += 1
                maxTime = max(maxTime, time)
        return fleets




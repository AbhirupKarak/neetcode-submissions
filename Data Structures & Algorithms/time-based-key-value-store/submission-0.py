class TimeMap:

    def __init__(self):
        self.timeStamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #here we store the values in timestamp as {key: (value, timestamp)}
        self.timeStamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #here we do binary search on the timestamp
        l = 0
        r = len(self.timeStamp[key]) - 1
        arr = self.timeStamp[key]
        ans = ""
        while(l <= r):
            mid = (l + r) // 2
            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]   #valid candidate
                l = mid + 1
            #we search for largest entry with value <= timestamp
            else:
                r = mid - 1
        return ans
        
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sort = list(freq.items())  # e.g. [(1, 3), (2, 2), (3, 1)]
        sort.sort(key = lambda pair : pair[1], reverse = True)
        res = [pair[0] for pair in sort[:k]]
        return res



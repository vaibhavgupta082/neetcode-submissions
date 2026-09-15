class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for num in nums:
            mp[num] = mp.get(num,0) + 1

        sorted_dict = dict(sorted(mp.items(), reverse = True ,key=lambda item: item[1]))

        res = (list(sorted_dict.keys())[:k])

        return res

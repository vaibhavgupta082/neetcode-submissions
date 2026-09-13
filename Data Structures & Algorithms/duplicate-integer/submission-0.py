class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = set()
        for i in range(0,len(nums)):
            if nums[i] in mp:
                return True
            else:
                mp.add(nums[i])
        return False
        
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        max_cnt = 0

        for num in nums:
            #found the start point 
            if num - 1 not in mp:
                curr_num = num
                cnt = 1
                while curr_num + 1 in mp:
                    cnt += 1
                    curr_num += 1
                max_cnt = max(max_cnt , cnt)
        return max_cnt

                
               



        
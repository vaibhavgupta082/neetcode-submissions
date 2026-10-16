class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b , c = a + 1, n - 1

            while b < c :
                curr_sum = nums[a] + nums[b] + nums[c]
                if curr_sum == 0:
                    res.append([nums[a],nums[b],nums[c]])
                    b += 1
                    c -= 1

                    while b < c and nums[b] == nums[b-1]:
                        b = b+ 1
                    while b < c and nums[c] == nums[c+1]:
                        c = c - 1
                                              
                elif curr_sum > 0:
                    c -= 1
                else:
                    b += 1
        return res
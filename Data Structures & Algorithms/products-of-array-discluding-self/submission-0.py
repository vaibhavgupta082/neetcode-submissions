class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l2r  = []
        res = []
        r2l = [1]*(n + 1)
        prdt = 1
        
        l2r.append(1)
        for i in range(n):
            prdt = l2r[-1] * nums[i]
            l2r.append(prdt)
        
        for i in range(n-1,-1,-1):
            r2l[i] = nums[i] * r2l[i] * r2l[i+1]

        # print(l2r)
        # print(r2l)

        for i in range(n):
            # print(i)
            val = l2r[i]*r2l[i+1]
            # print(val)
            res.append(val)
        # print(res)

        return res




        
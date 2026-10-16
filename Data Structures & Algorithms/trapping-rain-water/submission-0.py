class Solution:
    def trap(self, height: List[int]) -> int:
        l2r = [0]*len(height)
        r2l = [0]*len(height)
        water_sum = 0
        #populate l2r
        l2r[0] = height[0]
        for i in range(len(height)):
            if i > 0:
                l2r[i] = max( l2r[i-1] , height[i] )
        # print(l2r)

        #populate r2l
        r2l[-1] = height[-1]
        for j in range(len(height)-2, -1 , -1):
            r2l[j] = max(r2l[j+1], height[j])
        # print(r2l)

        for k in range(len(height)):
            water_sum += (min(l2r[k],r2l[k]) - height[k])

        return water_sum


        
        
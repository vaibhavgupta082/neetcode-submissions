class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # length of s2 < s1 --- return false
        # create a mp for s1 which will store the mapping
        if len(s2) < len(s1):
            return False
        
        mp_s1 = [0]*26
        mp_s2 = [0]*26
        win_s1 = len(s1)
        l , r = 0 ,0

        for i in range(len(s1)):
            mp_s1[ord(s1[i])-97] +=1

        while r<win_s1:
            mp_s2[ord(s2[r])-97] +=1
            r += 1
        
        while l<=r and r < len(s2):
            if mp_s2 == mp_s1:
                return True
            else:
                mp_s2[ord(s2[l])-97] = mp_s2[ord(s2[l])-97] - 1
                l += 1
                # FIXED: Update map with current 'r' first, then increment 'r'
                mp_s2[ord(s2[r])-97] +=1
                r += 1
                
        # FIXED: Check the very last window which was left unchecked when r reached len(s2)
        return mp_s2 == mp_s1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        for ch in s:
            if ch in mp1:
                mp1[ch] = mp1[ch] + 1
            else:
                mp1[ch] = 1

        for ch in t:
            if ch in mp2:
                mp2[ch] = mp2[ch] + 1
            else:
                mp2[ch] = 1
                
        return True if mp1 == mp2 else False 
    
        
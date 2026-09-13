class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r, l = 0 , 0
        mp = set()
        cnt = 0

        while l <= r and r < len(s):
            if s[r] not in mp:
                mp.add(s[r])
                r += 1
                cnt = max(cnt, r-l)
            else:
                mp.remove(s[l])
                l += 1
        return cnt

        
        
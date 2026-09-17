class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_arr = [0]*26
        res = []
        mp = defaultdict(list)

        for word in strs:
            # print(word)
            for ch in word:
                char_arr[ord(ch)-97] = char_arr[ord(ch)-97] + 1
            # key = (''.join(map(str , char_arr)))
            # print(key)
            mp[tuple(char_arr)].append(word)
            char_arr = [0]*26
        return (list(mp.values()))

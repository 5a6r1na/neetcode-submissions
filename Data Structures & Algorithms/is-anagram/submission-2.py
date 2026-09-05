class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
        
        for r in t:
            if r in dict_t:
                dict_t[r] += 1
            else:
                dict_t[r] = 1
        
        return dict_s == dict_t
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}
        dict_t = {}

        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
        
        for r in t:
            if r not in dict_s:
                return False
            elif r in dict_t:
                dict_t[r] += 1
            else:
                dict_t[r] = 1
        
        if dict_s == dict_t:
            return True
        else:
            return False
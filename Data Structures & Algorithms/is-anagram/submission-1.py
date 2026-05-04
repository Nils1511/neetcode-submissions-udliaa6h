class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}

        for char in s:
            set_s[char] = 1 + set_s.get(char, 0)
        
        for char in t:
            set_t[char] = 1 + set_t.get(char, 0)
        
        if set_s == set_t:
            return True
        
        return False
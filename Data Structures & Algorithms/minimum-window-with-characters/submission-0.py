class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left = 0
        
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have = 0
        need = len(countT)
        reslen = float('inf')
        res = [-1, -1]

        window = {}
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (right - left + 1) < reslen:
                    res = [left, right]
                    reslen = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left : right + 1] if reslen != float('inf') else ""

             
            
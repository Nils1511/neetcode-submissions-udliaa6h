class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        maxl = 0
        left = 0
        charmap = {}
        for right in range(len(s)):
            charmap[s[right]] = 1 + charmap.get(s[right], 0)
            maxf = max(maxf, charmap[s[right]])
            if right-left+1 - maxf > k:
                charmap[s[left]] -= 1
                left += 1
            maxl = max(maxl, right-left+1)
        return maxl

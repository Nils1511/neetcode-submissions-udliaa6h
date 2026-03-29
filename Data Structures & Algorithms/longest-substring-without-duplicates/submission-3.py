class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = {}
        start = 0
        maxlength = 0
        for end, char in enumerate(s):
            if char in charmap and charmap[char]>=start:
                start = charmap[char] + 1

            charmap[char] = end
            maxlength = max(maxlength, end - start +1)
        return maxlength

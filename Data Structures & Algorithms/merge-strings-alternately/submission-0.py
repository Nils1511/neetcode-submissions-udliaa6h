class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        x = min(m, n)
        res = ""
        for i in range(x):
            res += word1[i] + word2[i]

        if m > x:
            res += word1[x:]
        elif n > x:
            res += word2[x:]

        return res 

        
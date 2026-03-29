class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        ch_freq = [0] * 26
        for ch in s1:
            ch_freq[ord(ch) - ord('a')] += 1

        win_freq = [0] * 26
        for i in range(len(s1)):
            win_freq[ord(s2[i]) - ord('a')] += 1

        if ch_freq == win_freq:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            win_freq[ord(s2[right]) - ord('a')] += 1
            win_freq[ord(s2[left]) - ord('a')] -= 1

            if ch_freq == win_freq:
                return True
            
            right += 1
            left += 1
        
        return False
        
        
        
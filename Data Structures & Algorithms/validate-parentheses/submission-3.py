class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1 and s !=' ':
            return False
        dic = {')' : '(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in dic:
                if stack and dic[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
                
        
        return True if not stack else False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s: 
            if stack:
                if stack[-1] == '(' and c == ')':
                    stack.pop(-1)
                    continue
                elif stack[-1] == '[' and c == ']':
                    stack.pop(-1)
                    continue
                elif stack[-1] == '{' and c == '}':
                    stack.pop(-1)
                    continue
                else: 
                    stack.append(c)
                    
            if not stack:
                stack.append(c)
             
            
        if stack:
            return False
        return True
            
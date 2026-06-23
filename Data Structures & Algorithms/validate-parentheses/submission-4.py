class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{"}

        for c in s: 
            if c in closeToOpen.values():
                stack.append(c)
            else: 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            
        return len(stack) == 0
            
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = [] 
        result = 0
        while tokens: 
            token = tokens.pop(0) 
            try:
                stack.append(int(token))
            except ValueError:
                stack.append(token)

            if len(stack) < 3 or stack[-1] not in ["+", "-", "/", "*"]:
                continue      

            op, right, left = stack.pop(-1), stack.pop(-1), stack.pop(-1)

            match op:
                case "+":
                    stack.append(left + right)
                case "-":
                    stack.append(left - right)
                case "*":
                    stack.append(left * right)
                case "/":
                    stack.append(int(left / right))
            print(stack, left, op, right)
    
        return stack[0]



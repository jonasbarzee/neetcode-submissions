class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        mono_stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while mono_stack and mono_stack[-1][0] <= temp:
                mono_stack.pop() 
                
            if mono_stack:
                result[i] = mono_stack[-1][1] - i  

            mono_stack.append((temp, i))
            
        return result

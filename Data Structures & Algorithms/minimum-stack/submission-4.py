class MinStack:

    def __init__(self):
        self.stack = []
        self.counts = {}
        self.minVal = None 

    def push(self, val: int) -> None:
        self.stack.append(val) 

        if val not in self.counts:
            self.counts[val] = 1
        else:
            self.counts[val] += 1

        if self.minVal is not None:
            self.minVal = min(self.minVal, val)
        else:
            self.minVal = val  

    def pop(self) -> None:
        popped = self.stack.pop() 
        self.counts[popped] -= 1

        if self.counts[popped] == 0:
            self.counts.pop(popped)

        if popped == self.minVal and self.counts:
            self.minVal = min(self.counts) 
        if not self.counts:
            self.minVal = None 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
        

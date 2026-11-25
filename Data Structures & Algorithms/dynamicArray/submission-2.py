class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.items = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.items:
            self.resize()
        self.arr[self.items] = n
        self.items += 1


    def popback(self) -> int:
        self.items -= 1
        val = self.arr[self.items]
        self.arr[self.items] = None
        return val
 

    def resize(self) -> None:
        self.arr += [None] * self.capacity
        self.capacity *= 2


    def getSize(self) -> int:
        return self.items
        
    
    def getCapacity(self) -> int:
        return self.capacity

class Solution: 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []         
        cars = sorted([(pos, speed) for pos, speed in zip(position, speed)], reverse=True) 

        for car in cars:
            pos, spd = car[0], car[1]
            time = (target - pos) / spd 

            if not stack or time > stack[-1]:
                stack.append(time)      

        return len(stack)
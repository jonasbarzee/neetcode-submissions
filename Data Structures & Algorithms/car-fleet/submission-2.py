class Solution:
    def calcTime(self, target: int, position: int, speed: int) -> int:
        return (target - position) / speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []         
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort(reverse=True)  

        for car in cars:
            pos, speed = car[0], car[1]
            time = self.calcTime(target, pos, speed)
            # print(car, time)

            if not stack or time > stack[-1]:
                stack.append(time)     

            # print(stack)

        return len(stack)
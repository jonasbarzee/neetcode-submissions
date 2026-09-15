class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, spd) for pos, spd in zip(position, speed)], reverse=True)
        fleets = 0
        leader = 0.0  

        for car in cars:
            pos, spd = car[0], car[1]
            time = (target - pos) / spd

            if time > leader:
                fleets += 1
                leader = time

        return fleets   
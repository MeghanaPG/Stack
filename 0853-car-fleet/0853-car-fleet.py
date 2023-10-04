class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        fleets = 0 
        prev_time = -1 

        for pos, spd in cars:
            time_to_target = (target - pos) / spd 

            if time_to_target > prev_time:
                fleets += 1 
                prev_time = time_to_target
                
        return fleets 


        
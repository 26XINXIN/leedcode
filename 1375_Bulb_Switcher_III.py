class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        blue_times = 0
        last_on = 0
        for i in range(len(light)):
            last_on = max(light[i], last_on)
            
            if last_on == i + 1:
                blue_times += 1
                
        return blue_times
            
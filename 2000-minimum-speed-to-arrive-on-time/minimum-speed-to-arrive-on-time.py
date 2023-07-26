import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1

        hourDupe = hour 
        hourDupe = hourDupe - int(hour)
        print(hour,hourDupe)
        if hourDupe !=0:
            r = math.ceil(max(dist) / (hourDupe))
        else:
            r = max(dist)
        speed = int(r)
        print("max considered speed =",speed)
        if hour <= len(dist)-1:
            return -1

        while l<=r:

            mid = (l+r)//2

            time = 0
            for d in range(len(dist)-1) :
                time += math.ceil(dist[d]/mid)
            time += dist[-1]/mid

            print("For speed :",mid, "time taken = ", time)

            if time <= hour:
                speed = min(speed,mid)
                r = mid-1
            else:
                l = mid+1
            
            

        return int(speed)
#code
import math
T = int(input())
for i in range(T):
    h, m = list(map(float, input().split()))
    if(h == 12):
        h = 0
    if(m == 60):
        m = 0
        h += 1
    
    hour_angle = (h * 60 + m) * 0.5
    minute_angle = m* 6
    
    diff = abs(hour_angle - minute_angle)
    
    print(math.floor(min(360 - diff, diff)))
        

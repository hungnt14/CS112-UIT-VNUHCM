import math

INF = 99999999999.0
n = int(input())
points = []

hasNegativeY = False

def check(radius):
    global points

    mn = float(1e9)
    mx = float(-1e9)

    for i in points:
        if abs(i[1]) > 2 * radius: return False

        length = math.sqrt(abs(2 * radius * abs(i[1]) - i[1] * i[1]))
        if mn > i[0] + length: 
            mn = i[0] + length
        if mx < i[0] - length: 
            mx = i[0] - length

    return mn >= mx
            
def solve():
    l = 0.0
    r = INF
    ans = -1
    
    for i in range (300):
        mid = (l + r) / 2
        
        if check(mid):
            r = mid
        else:
            l = mid
    return l
         
    
for i in range(n):
    points.append(list(map(int, input().split())))
    if (points[-1][1] < 0):
        hasNegativeY = True
    else:
        if (hasNegativeY):
            print(-1)
            exit()

print(round(solve(), 2))
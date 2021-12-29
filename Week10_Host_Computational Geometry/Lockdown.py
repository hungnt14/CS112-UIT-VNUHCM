class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def __lt__ (self, b):
        if self.x < b.x:
            return True
        elif self.x == b.x and self.y < b.y:
            return True
        return False
        
def CCW(p1, p2, p3):
    return (p1.x-p2.x)*(p1.y+p2.y) +(p2.x-p3.x)*(p2.y+p3.y) + (p3.x-p1.x)*(p3.y+p1.y)

def find_convex_hull(a,n):
    def graham(a,n):
        halfHull = []
        for i in range(n):
            while len(halfHull) >= 2 and CCW(halfHull[-2], halfHull[-1], a[i]) > 0:
                halfHull.pop()
            halfHull.append(a[i])
        
        return halfHull
    
    S1 = graham(a,n)
    S2 = graham(list(reversed(a)),n)
    S1.extend(S2[1:-1])
    
    
    return S1
    
a = []
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    a.append(Point(x,y))

res = 0
while (True):
    a = sorted(a)
    convex_hull = sorted(find_convex_hull(a,n))
    if len(convex_hull) < 3:
        break
    res += 1
    pos = 0
    temp = []
    for i in range(n):
        if pos < len(convex_hull) and a[i].x == convex_hull[pos].x and a[i].y == convex_hull[pos].y:
            pos +=1
        else:
            temp.append(a[i])
    a = temp
    n = len(a)

print(res)
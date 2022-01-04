import math 

class pt2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod 
    def sqr(z):
        return z * z

    @staticmethod 
    def distance(p2d1, p2d2):
        return math.sqrt(
            pt2d.sqr(abs(p2d1.x - p2d2.x)) + \
            pt2d.sqr(abs(p2d1.y - p2d2.y)))

def x_comp(a):
    return a.x

def findt(core, lst_start, lst_end):
    if (lst_end - lst_start <= 3):
        mn = float('inf')
        for i in range (lst_start, lst_end - 1):
            for j in range (i + 1, lst_end):
                mn = min(mn, pt2d.distance(core[i], core[j]))
        
        return mn

    mid = core[int(lst_start + (lst_end - lst_start) // 2)]
    
    mnl = min(findt(core, int(lst_start), int(lst_start + (lst_end - lst_start) // 2)), \
        findt(core, int(lst_start + (lst_end - lst_start) // 2), int(lst_end)))
     
    part = []
    for i in range (lst_start, lst_end):
        if (abs(core[i].x - mid.x) < mnl):
            part.append(core[i])
    
    for i in range (len(part) - 1):
        for j in range (i + 1, len(part)):
            if part[i].y - part[j].y < mnl:
                mnl = min(mnl, pt2d.distance(part[i], part[j]))

    return mnl

n = int(input())
lst = []
for i in range (n):
    x, y = list(map(int,input().split()))
    lst.append(pt2d(x, y))

lst.sort(key = x_comp)
print(str(round(findt(lst, int(0), int(len(lst))), 3)))
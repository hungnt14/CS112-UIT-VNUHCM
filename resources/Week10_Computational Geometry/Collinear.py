n = int(input())
x = []
y = []
for i in range(n):
    x1, y1 =  map(int, input().split())
    x.append(x1)
    y.append(y1)

def solve(k, x, y): 
    a = []
    for i in range(k): 
        dy = y[i] - y[k];
        if (dy != 0): 
            ai = (x[i] - x[k]) / dy
            a.append(ai)
        else: 
            ai = 1e9  
            a.append(ai)
    
    a.sort()
    res = 0;
    count = 1;
    for i in range(1, k):
        if (a[i] != a[i-1]):
            res += int(count*(count-1) / 2)
            count = 0
        
        count += 1
    
    res += int(count*(count-1) / 2)
    return res

#-------------------------------

res = 0;

for i in range(2, n):
    res += solve(i, x, y)

print(res)
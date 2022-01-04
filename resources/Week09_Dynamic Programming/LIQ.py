n = int(input())
a = list(map(int, input(). split()))
f = []
r = 0
for i in range(n):
    t = 1
    for j in range(len(f)):
        if a[j]<a[i]: t= max(f[j] + 1, t)
    f.append(t)
    r = max(t,r)
print(r)
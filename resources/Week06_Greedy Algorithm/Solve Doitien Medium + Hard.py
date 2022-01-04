n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

# Recursive
d = [int(-1) for i in range(20105)]
def recursive(s, a, n):
    if s == 0:
        return 0
    if s < a[0]:
        return (int)(1e9)
    if d[s] != -1:
        return d[s]

    res = (int)(1e9)
    for i in range(n - 1, -1, -1):
        if s >= a[i]:
            res = min(res, recursive(s - a[i], a, n))
    d[s] = res + 1
    return d[s]

# Greedy
def greedy(s, a, n):
    res = 0
    for i in range(n - 1, -1, -1):
        while s >= a[i]:
            s -= a[i]
            res += 1
    if s == 0:
        return res
    else:
        return (int)(1e9)


# Greedy
s1 = s
val = (int)(1e6)
res1 = (s1 - val) // a[n - 1]
if res1 < 0:
    res1 = 0
s1 -= res1 * a[n - 1]
ans = (int)(1e9)
ans = min(ans, greedy(s1, a, n))
res1 += ans

# Greedy + recursive
s2 = s
val = a[n - 1] * 200
res2 = (s2 - val) // a[n - 1]
if res2 < 0:
    res2 = 0
s2 -= res2 * a[n - 1]
if n > 20:
    temp = []
    for i in range(0, 10):
        temp.append(a[i])
    for i in range(n - 1, n - 11, -1):
        temp.append(a[i])
    n = 20
    a = temp
res2 += recursive(s2, a, n)
print(min(res1, res2))
md = 132864579
mtx_a = [[0, 1], [1, 1]]

def smtx_mult(a, b):
    c = [[0, 0], [0, 0]]
    for i in range (2):
        for j in range (2):
            for k in range (2):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= md

    return c

def smtx_pw(z):
    global mtx_a
    if (z == 1): 
        return mtx_a
    
    tmp = smtx_pw(z // 2)
    tmp = smtx_mult(tmp, tmp)

    if (z % 2 == 1):
        tmp = smtx_mult(tmp, mtx_a)

    return tmp

def get(n):
    if n == 0:
        return 1
    fn = smtx_pw(n)
    return fn[1][1]

n = int(input())
core = list(map(int, input().split()))

for i in core:
    print(get(i), end = " ")
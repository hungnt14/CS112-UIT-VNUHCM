mx_sz = 2 * 10 ** 5 + 111
mod = 10 ** 9 + 7

dp = [1] * mx_sz
for i in range(10, mx_sz):
    dp[i]= (dp[i - 9] + dp[i - 10]) % mod
    
for inp in [*open(0)][1:]:
    n, m = inp.split()
    m = int(m)
    ans = 0
    for c in n:
        ans = (ans + dp[m + int(c)]) % mod
    print(ans)
n = int(input())
MOD = int(1e9 + 7)

f = [[0, 0, 0] for i in range(int(1e5+1))]

f[1][0] = 1
f[1][1] = 1
f[1][2] = 1

for i in range(2, n + 1):
		for c in range(0, 3):
			f[i][c] += f[i - 1][0]
			if(c != 1): f[i][c] += f[i - 1][1]
			f[i][c] += f[i - 1][2]
			f[i][c] %= MOD

res = f[n][0] + f[n][1] + f[n][2]
print(res % MOD)
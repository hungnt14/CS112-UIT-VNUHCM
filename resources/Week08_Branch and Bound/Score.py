s, k, n = map(int, input().split())
givenScore = [list(map(int, input().split())) for _ in range(n)]

def solve(i, sum, pickedScore):
    if (sum > s):
        return False
    if (i == k):
        if (sum == s):
            return True
        else:
            return False
    
    ret = 0
    for j in range(n):
        if (i == 0):
            ret = max(ret, solve(i + 1, sum + givenScore[j][i], j))
        else:
            if (givenScore[j][i] >= givenScore[pickedScore][i - 1]):
                ret = max(ret, solve(i + 1, sum + givenScore[j][i], j))    
    return ret

print("YES" if solve(0, 0, 0) else "NO")
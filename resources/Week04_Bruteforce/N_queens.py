n = int(input())
a = n*[0]
ans = 0
def Ok(x2,y2):
    for i in range(x2):
        if(a[i] == y2 or abs(i-x2) == abs(a[i] - y2) ):
            return False
    return True

def Try(i,n):
    global ans
    for j in range(n):
        if(Ok(i,j)):
            a[i] = j
            if (i==n-1): 
                ans +=1
            Try(i+1,n)

Try(0,n)
print(ans)
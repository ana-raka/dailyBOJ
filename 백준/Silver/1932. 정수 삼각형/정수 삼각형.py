n = int(input())
dp = [[] for i in range(n)]
res = []
for i in range(n):
    res.append(list(map(int,input().split())))
dp[0] = res[0]
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i].append(dp[i-1][0]+ res[i][0])
        elif j == (i):
            dp[i].append(dp[i-1][-1] + res[i][-1])
        else:
            dp[i].append(max(dp[i-1][j] + res[i][j] , dp[i-1][j-1] + res[i][j]))
print(max(dp[n-1]))


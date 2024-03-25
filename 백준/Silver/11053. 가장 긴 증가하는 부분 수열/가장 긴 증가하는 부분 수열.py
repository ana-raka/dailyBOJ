import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = [0 for _ in range(n)]
numl = list(map(int,input().split()))
for i in range(n):
    max_val = 1
    if i == 0:
        res[i] = 1
        continue
    for j in range(i - 1, -1, -1):
        if numl[j] < numl[i]:
            max_val = max(max_val, res[j] + 1)
    res[i] = max_val
print(max(res))
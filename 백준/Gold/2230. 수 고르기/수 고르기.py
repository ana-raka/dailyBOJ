import sys
input = sys.stdin.readline

n, m = map(int,input().split())
numl = []
for _ in range(n):
    numl.append(int(input().rstrip()))
numl.sort()
left = right = 0
res = 10000000001
while left != n and right != n:
    if numl[right] - numl[left] >= m:
        res = min(res, numl[right] - numl[left])
        left += 1
    elif numl[right] - numl[left] < m:
        right += 1
print(res)
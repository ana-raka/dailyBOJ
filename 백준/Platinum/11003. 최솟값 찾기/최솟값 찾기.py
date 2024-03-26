import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n, l = map(int,input().split())
numl = list(map(int,input().split()))

for i in range(n):
    if q  and q[0][1] <= i - l :
        q.popleft()
    while len(q) > 0 and numl[i] < q[-1][0]:
        q.pop()
    q.append((numl[i], i ))

    print(q[0][0], end=" ")
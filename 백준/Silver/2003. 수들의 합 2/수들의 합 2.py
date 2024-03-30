import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
numl = list(map(int,input().split()))
left = right = cnt = 0
res = 0
while right <= n:
    if res < m:
        if right < n:
            res += numl[right]
        right += 1
    elif res >= m:
        if res == m:
            cnt += 1
        res -= numl[left]
        left += 1
print(cnt)
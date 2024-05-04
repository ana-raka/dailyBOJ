import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        now , cnt = q.popleft()
        if now == b:
            print(cnt)
            exit()
        if now * 2 <= 100000 and visit[now * 2] == 0:
            q.append((now * 2, cnt))
        for i in range(-1, 2, 2):
            if 0 <= now + i <= 100000 and visit[now + i] == 0:
                visit[now + i] = 1
                q.append((now + i , cnt + 1))
q = deque()
a , b = map(int,input().split())
if a > b:
    print(a - b)
    exit()
visit = [0 for _ in range(100001)]
q.append((a,0))
bfs()
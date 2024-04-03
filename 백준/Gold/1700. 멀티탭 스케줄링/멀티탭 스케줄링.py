import sys
input = sys.stdin.readline
from queue import PriorityQueue

n, m = map(int,input().split())
visit = [0 for _ in range(101)]
numl = list(map(int,input().split()))
num_cnt = 0
res = 0
for i in range(len(numl)):
    if visit[numl[i]] == 1:
        continue
    if num_cnt == n:
        dic = [0 for _ in range(101)]
        num_cnt -= 1
        min_idx = -1
        for j in range(i,len(numl)):
            if visit[numl[j]] == 1 and dic[numl[j]] == 0:
                dic[numl[j]] = j
        for k in range(1,101):
            if dic[k] == 0 and visit[k] == 1:
                min_idx = k
                break
            elif dic[min_idx] < dic[k]:
                min_idx = k
        visit[min_idx] = 0
        res += 1
    visit[numl[i]] = 1
    num_cnt += 1
print(res)
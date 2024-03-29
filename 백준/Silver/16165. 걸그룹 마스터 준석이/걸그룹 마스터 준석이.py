import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
dic = {}
for i in range(n):
    team_name = input().rstrip()
    dic[team_name] = []
    for j in range(int(input().rstrip())):
        name = input().rstrip()
        dic[team_name].append(name)
        dic[name] = team_name
for i in range(m):
    g_name = input().rstrip()
    p_num = int(input().rstrip())
    if p_num == 1:
        print(dic[g_name])
    else:
        for name in sorted(dic[g_name]):
            print(name)
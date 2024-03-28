import sys
input = sys.stdin.readline
from collections import OrderedDict

n, m = map(int,input().split())
dic = {}
for i in range(m):
    stdid = input().rstrip()
    try:
        dic[stdid][1] = i
    except:
        dic[stdid] = [1,i]
cnt = 0
stdlist = sorted(dic.items(), key= lambda x : x[1][1])
for stdid, val in stdlist:
    if val[0] == 1:
        print(stdid)
        cnt += 1
    if cnt == n:
        exit()
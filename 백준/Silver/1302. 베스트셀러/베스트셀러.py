import sys
input = sys.stdin.readline

dic = {}
for i in range(int(input().rstrip())):
    now = input().rstrip()
    try:
        dic[now] += 1
    except:
        dic[now] = 0
numl = list(dic.items())
numl.sort(key= lambda x: (-x[1],x[0]))
print(numl[0][0])
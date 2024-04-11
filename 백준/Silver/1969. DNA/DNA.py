import sys
input = sys.stdin.readline

n, m = map(int,input().split())
st = ""
res_str = ""
res = 0
for _ in range(n):
    st += input().rstrip()
for i in range(m):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    min_num = 0
    plus_st = st[0]
    for j in range(i, len(st), m):
        dic[st[j]] += 1
    for key , val in dic.items():
        if min_num < val:
            plus_st = key
            min_num = val
    res += n - min_num
    res_str += plus_st
print(res_str, res, sep="\n")
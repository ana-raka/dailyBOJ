import sys
input = sys.stdin.readline

res = []
idx = 0
is_blank = False
while True:
    numl = list(input().split())
    if len(numl) == 0:
        if is_blank:
            break
        is_blank = True
        continue
    if idx == 0:
        numl.pop(0)
        idx += 1
    for num in numl:
        res.append(int(num[-1::-1]))
    is_blank = False
res.sort()
for num in res:
    print(num)
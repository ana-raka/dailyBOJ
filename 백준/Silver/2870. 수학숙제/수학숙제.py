import sys
input = sys.stdin.readline

res = []
for _ in range(int(input().rstrip())):
    stl = input().rstrip()
    temp_st = ""
    for st in stl:
        try:
            if 0 <= int(st) <= 27:
                temp_st += st
        except:
            if temp_st != "":
                val = int(temp_st)
                res.append(int(temp_st))
                temp_st = ""
    else:
        if temp_st != "":
            val = int(temp_st)
            res.append(int(temp_st))
res.sort()
print(*res, sep="\n")
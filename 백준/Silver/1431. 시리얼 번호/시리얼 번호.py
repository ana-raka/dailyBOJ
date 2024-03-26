import sys
input = sys.stdin.readline
def sum(numl):
    res = 0
    for i in numl:
        try:
            res += int(i)
        except:
            continue
    return res
serial = []
for _ in range(int(input().rstrip())):
    serial.append(input().rstrip())
serial.sort(key= lambda x : (len(x),sum(x),x))
print(*serial,sep='\n')

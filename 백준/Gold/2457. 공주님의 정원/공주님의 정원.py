import sys
input = sys.stdin.readline


cnt = 1
flowerlist = [[] for _ in range(13)]
stack = []
for i in range(int(input().rstrip())):
    flower = list(map(int,input().split()))
    flowerlist[flower[0]].append(flower)
for flw in flowerlist:
    flw.sort(key=lambda x: (-x[2], -x[3], x[1]))
for i in range(3,0,-1):
    if i == 3:
        for ckflower in flowerlist[i]:
            if ckflower[1] == 1:
                stack.append(ckflower + [cnt])
                break
    else:
        if len(stack) == 0 and flowerlist[i]:
            stack.append(flowerlist[i][0] + [cnt])
        else:
            if flowerlist[i] and flowerlist[i][0][2] > stack[-1][2]:
                stack.pop()
                stack.append(flowerlist[i][0] + [cnt])
            elif flowerlist[i] and flowerlist[i][0][2] == stack[-1][2] and flowerlist[i][0][3] >= stack[-1][3]:
                stack.pop()
                stack.append(flowerlist[i][0] + [cnt])
else:
    if len(stack) == 0:
        print(0)
        exit()

while True:
    cnt += 1
    if cnt > 365 and stack[-1][2] < 12:
        print(0)
        exit()
    if stack[-1][2] >= 12:
        print(len(stack))
        exit()
    for i in range(stack[-1][2], stack[-1][0]-1, -1):
        if i == stack[-1][2]:
            for ckflower in flowerlist[i]:
                if ckflower[1] <= stack[-1][3]:
                    stack.append(ckflower + [cnt])
                    break
        else:
            if stack[-1][4] == cnt:
                if flowerlist[i] and flowerlist[i][0][2] > stack[-1][2]:
                    stack.pop()
                    stack.append(flowerlist[i][0] + [cnt])
                elif flowerlist[i] and flowerlist[i][0][2] == stack[-1][2] and flowerlist[i][0][3] >= stack[-1][3]:
                    stack.pop()
                    stack.append(flowerlist[i][0] + [cnt])
            else:
                if flowerlist[i]:
                    stack.append(flowerlist[i][0] + [cnt])

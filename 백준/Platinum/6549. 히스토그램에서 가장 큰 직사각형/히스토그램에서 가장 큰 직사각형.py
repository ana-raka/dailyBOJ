import sys
input = sys.stdin.readline

while True:
    numl = list(map(int,input().split()))
    if numl[0] == 0:
        break
    res = 0
    numl.pop(0)
    stack = [[1,1,0]]
    idx = 0
    for num in numl:
        vool = False
        idx += 1
        total = 0
        prev= 0
        num_idx = 0
        if len(stack) == 0:
            stack.append([num,idx,0])
            continue
        while stack and stack[-1][0] >= num:
            leng, num_idx, prev = stack.pop()
            cnt = (idx - num_idx) + prev
            res = max(res, leng * cnt)
            vool = True
        if vool:
            total += prev + (idx - num_idx)  # 문제 부분
        stack.append([num,idx, total])
    for num_cnt in stack:
        res = max(res, num_cnt[0] * ((idx - num_cnt[1]+ 1) + num_cnt[2]))
    print(res)
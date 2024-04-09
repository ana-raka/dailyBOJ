import sys
input = sys.stdin.readline

strl = input().rstrip()
target = input().rstrip()
idx = 0
cnt = 0
while idx < len(strl):
    if strl[idx] == target[0]:
        if strl[idx:idx+len(target)] == target:
            cnt += 1
            idx += len(target)
            continue
    idx += 1
print(cnt)
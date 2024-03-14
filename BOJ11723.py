import sys
input = sys.stdin.readline

cnum = int(input().rstrip())
s = [0 for i in range(21)]
for i in range(cnum):
    cmd = list(input().split())
    if len(cmd) == 1:
        if cmd[0] == "all":
            s = [1 for i in range(21)]
        else:
            s = [0 for i in range(21)]
    else:
        target_num = int(cmd[1])
        if cmd[0] == "add":
            s[target_num] = 1
        elif cmd[0] == "remove":
            s[target_num] = 0
        elif cmd[0] == "check":
            print(s[target_num])
        elif cmd[0] == "toggle":
            if s[target_num] == 0:
                s[target_num] = 1
            else:
                s[target_num] = 0
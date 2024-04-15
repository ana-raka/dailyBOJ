import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    dic = {}
    goesl = list(input().split())
    while True:
        goes = list(input().split())
        if " ".join(goes) == "what does the fox say?":
            for goes in goesl:
                try:
                    if dic[goes] == 0:
                        continue
                except:
                    print(goes, end=" ")
            print()
            break
        dic[goes[2]] = 1
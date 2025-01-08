# 알고리즘: 
# 시간복잡도: O(N)
# 자료구조: 스택

def solution(s):
    temp = []
    answer = True
    s = list(s)
    while s:
        if s[-1] == ")":
            temp.append(s.pop())
        else:
            if temp:
                temp.pop()
            else:
                return False
            s.pop()
    if temp:
        answer = False
    return answer
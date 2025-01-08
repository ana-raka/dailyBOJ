# 알고리즘: 정렬
# 시간복잡도: O(N)
# 자료구조: 큐
from collections import deque

def solution(priorities, location):
    deq = deque()
    for i in range(len(priorities)):
        if i == location:
            deq.append((priorities[i], True))
            continue
        deq.append((priorities[i], False))
    priorities.sort()
    cnt = 1
    while deq:
        if deq[0][0] == priorities[-1] and deq[0][1]:
            break
        elif deq[0][0] == priorities[-1]:
            deq.popleft()
            priorities.pop()
            cnt += 1
        else:
            deq.rotate(-1)        
    return cnt
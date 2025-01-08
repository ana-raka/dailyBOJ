# 알고리즘: ?
# 시간복잡도: O(N)
# 자료구조: 테크
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt != 0:
             answer.append(cnt)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    return answer
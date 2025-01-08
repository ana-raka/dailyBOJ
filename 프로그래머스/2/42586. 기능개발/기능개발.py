# 알고리즘: ?
# 시간복잡도: O(N)
# 자료구조: 테크
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 0
    while progresses:
        cnt = 0
        while progresses and progresses[0] + ( day * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt != 0:
             answer.append(cnt)
        day += 1
    return answer
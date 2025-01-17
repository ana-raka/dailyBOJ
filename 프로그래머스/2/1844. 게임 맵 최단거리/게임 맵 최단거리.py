# 알고리즘: BFS
# 시간복잡도: O(N * M)
# 자료구조: 큐, 그래프
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    result_map = [[0 for _ in range(m)] for _ in range(n)]
    result_map[0][0] = 1
    def BFS():
        mvx = [1,-1,0,0]
        mvy = [0,0,1,-1]
        que = deque([(0,0)])
        while que:
            y, x = que.popleft()
            for i in range(4):
                my = y + mvy[i]
                mx = x + mvx[i]
                if 0 <= my <= n-1 and 0 <= mx <= m-1:
                    if maps[my][mx] == 1 and result_map[my][mx] == 0:
                        result_map[my][mx] = result_map[y][x] + 1
                        que.append((my,mx))
    BFS()
    return result_map[n-1][m-1] if result_map[n-1][m-1] != 0 else -1
# 알고리즘: BFS
# 시간복잡도: 
# 자료구조: 그래프, 큐

from collections import deque
            
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0 for _ in range(102)] for _ in range(102)]
    for lx, ly, rx, ry in rectangle:
        lx, ly, rx, ry = lx * 2, ly * 2, rx * 2, ry * 2
        for y in range(ly, ry + 1):
            for x in range(lx, rx + 1):
                if x == lx or x == rx or y == ly or y == ry: 
                    if graph[y][x] == 0: 
                        graph[y][x] = 1
                else:  
                    graph[y][x] = -1
    def BFS():
        graph[characterY * 2][characterX * 2] = 1
        que = deque([(characterY * 2, characterX * 2)])
        mv = [(0,1),(0,-1),(1,0),(-1,0)]
        while que:
            y,x = que.popleft()
            if (y, x) == (itemY * 2, itemX * 2): 
                return graph[y][x] // 2 
            for my, mx in mv:
                mvy = my + y
                mvx = mx + x
                if 1 <= mvy < 102 and 1 <= mvx < 102:
                    if graph[mvy][mvx] == 1:
                        graph[mvy][mvx] = graph[y][x] + 1
                        que.append((mvy, mvx))
    return BFS()
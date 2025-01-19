# 알고리즘: BFS
# 시간복잡도: O()
# 자료구조: 그래프
from collections import defaultdict, deque
def solution(n, edge):
    node_dict = defaultdict(list)
    dist_dict = defaultdict(int)
    que = deque([(1,0)])
    is_visted = [False] * (n + 1)
    for x, y in edge:
        node_dict[x].append(y)
        node_dict[y].append(x)
    is_visted[1] = True
    while que:
        now_node, dist = que.popleft()
        for next_node in node_dict[now_node]:
            if not is_visted[next_node]:
                que.append((next_node, dist + 1))
                is_visted[next_node] = True
                dist_dict[dist+1] += 1
                
    return dist_dict[dist]
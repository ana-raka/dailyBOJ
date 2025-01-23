# 알고리즘: 크루스칼
# 시간복잡도: O(NlogN)
# 자료구조: 그래프
def solution(n, costs):
    def union_find(n):
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
        return find, union
    costs.sort(key = lambda x : x[2])
    find, union = union_find(n)
    answer = 0
    edge_count = 0
    for u, v, cost in costs:
        if find(u) != find(v):
            union(u,v)
            answer += cost
            edge_count += 1
            if edge_count == n -1:
                break
                
    return answer
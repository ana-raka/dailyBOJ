# 알고리즘: 완전탐색
# 시간복잡도: O(N)
# 자료구조: 리스트
def solution(sizes):
    rotated_size = [[max(h,v), min(h,v)] for h, v in sizes]
    max_h = 0  
    max_v = 0
    for h, v in rotated_size:
        max_h = max(max_h, h)
        max_v = max(max_v, v)
    return max_h * max_v
# 알고리즘: 정렬, 그리디
# 시간복잡도: O(NlogN)
# 자료구조: 리스트
def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001 
    answer = 0    
    for start, end in routes:
        if start > camera:
            camera = end
            answer += 1
    return answer
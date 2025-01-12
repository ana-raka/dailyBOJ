# 알고리즘: 완전탐색
# 시간복잡도: O(N) 
# 자료구조: 리스트
def solution(brown, yellow):
    answer = []
    for h in range(yellow, 0, -1):
        if (h + 2) * 2 + (yellow / h) * 2 == brown:
            answer.append(h+2)
            answer.append(yellow / h + 2)
            break
    return answer
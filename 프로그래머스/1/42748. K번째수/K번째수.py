# 알고리즘: 정렬
# 시간복잡도: O(NlogN)
# 자료구조: 리스트
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        target_list = array[i-1:j]
        target_list.sort()
        answer.append(target_list[k-1])
    return answer
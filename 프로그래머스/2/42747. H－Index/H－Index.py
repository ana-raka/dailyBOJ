# 알고리즘: 정렬
# 시간복잡도: O(NlogN)
# 자료구조: 리스트
def solution(citations):
    sorted_citations = sorted(citations, reverse = True)
    for i in range(len(sorted_citations)):
        if sorted_citations[i] < i + 1:
            return i
    return len(sorted_citations)
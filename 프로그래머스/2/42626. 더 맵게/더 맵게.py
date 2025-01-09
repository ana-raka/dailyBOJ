# 알고리즘: 우선순위 큐
# 시간복잡도: O(NlogN)
# 자료구조: 힙
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first_scov = heapq.heappop(scoville)
        second_scov = heapq.heappop(scoville)
        heapq.heappush(scoville, first_scov + (second_scov * 2))
        answer += 1
    return answer
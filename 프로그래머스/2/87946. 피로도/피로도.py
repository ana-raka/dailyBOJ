# 알고리즘: 정렬
# 시간복잡도: O(N!)
# 자료구조: permutations
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons, len(dungeons)):
        temp_k = k
        cnt = 0
        for dungeon in per:
            if temp_k >= dungeon[0]:
                temp_k -= dungeon[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer
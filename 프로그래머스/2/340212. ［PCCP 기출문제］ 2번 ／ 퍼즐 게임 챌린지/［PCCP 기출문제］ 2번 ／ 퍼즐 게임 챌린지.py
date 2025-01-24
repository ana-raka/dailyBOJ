# 알고리즘: 이분탐색
# 시간복잡도: O(log(maxN)) N은 난이도
# 자료구조: 
def solution(diffs, times, limit):
    def can_solve(level):
        total = 0
        prev = 0
        for diff, time in zip(diffs,times):
            if diff <= level:
                total += time
            else:
                total += (diff - level) * (prev + time) + time
            prev = time
            
            if total > limit:
                return False
        return True
    left, right = 1, max(diffs)
    answer = right
    while left <= right:
        mid = (left + right ) // 2
        if can_solve(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
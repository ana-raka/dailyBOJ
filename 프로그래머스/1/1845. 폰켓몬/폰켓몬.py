# 알고리즘: 해시
# 시간복잡도: ?
# 자료구조: 해시
def solution(nums):
    pmon_set = set(nums)
    return min(len(nums)/2 , len(pmon_set))
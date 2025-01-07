# 알고리즘: 해시
# 시간복잡도: ?
# 자료구조: 해시
def solution(nums):
    pmon_set = set(nums)
    if len(pmon_set) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(pmon_set)
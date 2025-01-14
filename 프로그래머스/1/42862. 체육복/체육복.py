# 알고리즘: 그리디
# 시간복잡도: O(NlogN)
# 자료구조: 집합, 리스트

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for lost_student in sorted(lost_set): 
        if lost_student - 1 in reserve_set:
            reserve_set.remove(lost_student - 1)
            lost_set.remove(lost_student)
        elif lost_student + 1 in reserve_set:
            reserve_set.remove(lost_student + 1)
            lost_set.remove(lost_student)
    return n - len(lost_set)
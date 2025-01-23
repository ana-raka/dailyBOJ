# 알고리즘: 수학
# 시간복잡도: O(N^2)
# 자료구조: 리스트
def solution(lottos, win_nums):
    win_cnt = 0
    blank_cnt = 0
    rank = [6] + [i for i in range(6,0,-1)]
    for lotto in lottos:
        if lotto == 0:
            blank_cnt += 1
        if lotto in win_nums:
            win_cnt += 1     
    answer = [rank[win_cnt + blank_cnt], rank[win_cnt]]
    return answer
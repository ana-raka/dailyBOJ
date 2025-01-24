# 알고리즘: 구현
# 시간복잡도: O()
# 자료구조: 리스트
def solution(wallet, bill):
    h, v = max(wallet), min(wallet)
    answer = 0
    while True:
        bill_h, bill_v = max(bill), min(bill)
        if bill_h <= h and bill_v <= v:
            break
        bill = [bill_h // 2 , bill_v]
        answer += 1
    return answer
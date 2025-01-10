# 알고리즘: 완전탐색
# 시간복잡도: O(N)
# 자료구조: 리스트
def is_answer(answer, student, idx):
    if answer == student[idx % len(student)]:
        return 1
    return 0

def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    result_cnt = [0] * 3
    for idx , answer_num in enumerate(answers):
        result_cnt[0] += is_answer(answer_num, s1, idx)
        result_cnt[1] += is_answer(answer_num, s2, idx)
        result_cnt[2] += is_answer(answer_num, s3, idx)
    max_score = max(result_cnt)
    answer = [i + 1 for i in range(3) if result_cnt[i] == max_score]
    return answer
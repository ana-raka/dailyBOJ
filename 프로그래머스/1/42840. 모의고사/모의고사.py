# 알고리즘: 완전탐색
# 시간복잡도: O(N)
# 자료구조: 리스트
def is_correct(answer, student, idx):
    return answer == student[idx % len(student)]

def solution(answers):
    patterns = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]
               ]
    result_cnt = [0] * 3
    for idx , answer_num in enumerate(answers):
        for i in range(3):
            if is_correct(answer_num, patterns[i], idx):
                result_cnt[i] += 1
    max_score = max(result_cnt)
    answer = [i + 1 for i in range(3) if result_cnt[i] == max_score]
    return answer
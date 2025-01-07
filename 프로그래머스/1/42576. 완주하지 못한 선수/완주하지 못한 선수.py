# 알고리즘: 해시
# 시간 복잡도:
# 자료구조: 해시

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    else:
        return participant[-1]
    
            
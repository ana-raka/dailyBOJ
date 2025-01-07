# 알고리즘: 정렬, 해시
# 시간복잡도: O(N*logN)
# 자료구조: 디폴트 딕셔너리, 리스트
from collections import defaultdict

def solution(genres, plays):
    plays_dict = defaultdict(int)
    music_dict = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        plays_dict[genres[i]] += plays[i]
        music_dict[genres[i]].append((i, plays[i]))
    
    sorted_genres = sorted(plays_dict.items(), key=lambda x: -x[1])
    
    for genre, play in sorted_genres:
        music_dict[genre].sort(key=lambda x: (-x[1], x[0]))
        
        for i in range(min(2, len(music_dict[genre]))):
            answer.append(music_dict[genre][i][0])
    
    return answer
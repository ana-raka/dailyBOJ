# 알고리즘: BFS
# 시간복잡도: O(N^2)
# 자료구조: 큐, 집합, 딕셔너리

from collections import defaultdict, deque

def solution(begin, target, words):
    word_set = set(words)
    char_dict = defaultdict(set)
    for word in words:
        for i, char in enumerate(word):
            char_dict[i].add(char)    
    def BFS():
        que = deque([(begin, 0)])
        while que:
            now_word, cnt = que.popleft()
            if now_word == target:
                return cnt
            now_word = list(now_word)
            for i in range(len(now_word)):
                original_char = now_word[i]
                for char in char_dict[i]:
                    if char != original_char:
                        now_word[i] = char
                        changed_word = "".join(now_word)
                        if changed_word in word_set:
                            word_set.remove(changed_word)
                            que.append((changed_word, cnt + 1))
                now_word[i] = original_char
        return 0
    return BFS()
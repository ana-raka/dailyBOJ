# 알고리즘: 완전탐색
# 시간복잡도: O()
# 자료구조: 
def generate_words(vowels, max_length, current_word, word_list):
    if len(current_word) > max_length: 
        return

    if current_word:
        word_list.append(current_word)

    for vowel in vowels: 
        generate_words(vowels, max_length, current_word + vowel, word_list)

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U'] 
    word_list = []  
    max_length = 5  

    generate_words(vowels, max_length, "", word_list)  
    word_list.sort() 

    return word_list.index(word) + 1 
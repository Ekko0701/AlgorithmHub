def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def dfs(current_word):
        if len(current_word) > 5:
            return
        words.append(current_word)
        for vowel in vowels:
            dfs(current_word + vowel)
    
    dfs("")
    words.sort()
    return words.index(word)
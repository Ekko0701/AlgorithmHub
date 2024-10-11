from collections import Counter

def solution(want, number, discount):
    answer = 0
    dictionary = Counter(dict(zip(want, number)))
    
    for i in range(len(discount) - 9):
        dictionary_dummy = Counter(discount[i: i+10])
        
        if dictionary_dummy == dictionary:
            answer += 1
    
    return answer
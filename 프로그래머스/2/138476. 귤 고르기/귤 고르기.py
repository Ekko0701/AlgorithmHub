from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counter = sorted(counter.values(), reverse = True)
    
    for i in counter:
        k -= i
        answer += 1
        
        if k <= 0:
            break
    return answer
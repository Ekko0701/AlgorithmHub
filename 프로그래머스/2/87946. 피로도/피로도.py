from itertools import permutations

def solution(k, dungeons):
    answer = -1
    cases = permutations(dungeons)
    print(cases)
    for case in cases:
        fatigue = k
        count = 0
        
        for min_fatigue, consumption in case:
            if fatigue >= min_fatigue:
                fatigue -= consumption
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer
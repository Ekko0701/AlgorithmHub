def solution(n, words):
    
    for x in range(1, len(words)):
        if words[x][0] != words[x-1][-1]  or words[x] in words[:x]:
            return [(x%n) + 1, (x//n) + 1]
            
    return [0, 0]
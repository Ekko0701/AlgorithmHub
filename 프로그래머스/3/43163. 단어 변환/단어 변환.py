from collections import deque

def solution(begin, target, words):
    def one_letter_difference(word1, word2):
        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return diff_count == 1
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        current, count = queue.popleft()
        
        if current == target:
            return count
        
        for word in words:
            if word not in visited and one_letter_difference(current, word):
                visited.add(word)
                queue.append((word, count + 1))
            
    return 0
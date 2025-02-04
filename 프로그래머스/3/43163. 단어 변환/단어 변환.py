from collections import deque

def solution(begin, target, words):
    def check_difference(x, y):
        check = sum([w1 != w2 for w1, w2 in zip(x, y)])
        return check == 1
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        current, count = queue.popleft()
        
        if current == target:
            return count
        
        for word in words:
            if word not in visited and check_difference(current, word):
                visited.add(word)
                queue.append((word, count + 1))
            
    
    return 0
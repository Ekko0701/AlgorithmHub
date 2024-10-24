from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(zip(progresses, speeds))
    
    while queue:
        # 배포일 수를 계산
        day = 0
        while queue[0][0] + queue[0][1] * day < 100:
            day += 1
        
        # 배포할 수 있는 작업 수 계산
        count = 0
        while queue and queue[0][0] + queue[0][1] * day >= 100:
            queue.popleft()
            count += 1
        
        answer.append(count)
    
    return answer
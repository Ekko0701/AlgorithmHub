from collections import deque

def solution(priorities, location):
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    count = 0

    while queue:
        current = queue.popleft()

        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == location:
                return count
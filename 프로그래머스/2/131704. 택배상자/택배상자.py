from collections import deque

def solution(order):
    answer = 0
    sub_belt = deque()
    order_idx = 0
    current_box = 1
    sub_belt.append(0)

    while order_idx < len(order):
        if order[order_idx] == current_box:
            answer += 1
            order_idx += 1
            current_box += 1
        elif order[order_idx] == sub_belt[-1]:
            answer += 1
            sub_belt.pop()
            order_idx += 1
        elif order[order_idx] > current_box:
            sub_belt.append(current_box)
            current_box += 1
        else:
            break
        
    return answer

print(solution([3, 2, 1, 4, 5]))

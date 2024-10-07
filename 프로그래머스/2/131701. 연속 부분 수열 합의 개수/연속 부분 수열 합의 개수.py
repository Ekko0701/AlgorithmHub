def solution(elements):
    result = set()
    answer = 0
    for i in range(len(elements)):
        current_sum = 0
        for j in range(len(elements)):
            current_sum += elements[(i + j) % len(elements) ]
            result.add(current_sum)
                   
    answer = len(result)
    return answer
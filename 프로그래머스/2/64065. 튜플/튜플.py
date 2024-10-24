from collections import Counter

def solution(s):
    numbers = []
    number = ""
    for char in s:
        if char.isdigit():
            number += char
        else:
            if number:
                numbers.append(number)
                number = ""
    if number:
        numbers.append(number)
    count = Counter(numbers)
    return list(map(int, [k for k, v in sorted(count.items(), key=lambda x: x[1], reverse=True)]))
from collections import Counter
import re

def create_set(x):
    x = x.lower()
    set = []
    for i in range(len(x) - 1):
        two = x[i: i+2]
        if re.match(r'^[a-z]{2}$', two):
            set.append(two)
    return set

def solution(str1, str2):
    answer = 0
    first_set = create_set(str1)
    second_set = create_set(str2)

    first_set_counter = Counter(first_set)
    second_set_counter = Counter(second_set)

    intersection = first_set_counter & second_set_counter
    union = first_set_counter | second_set_counter

    inter_size = sum(intersection.values())
    union_size = sum(union.values())

    if union_size == 0:
        return 65536
    jaccard = inter_size / union_size
    return int(jaccard * 65536)
    return answer
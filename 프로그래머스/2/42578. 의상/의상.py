def solution(clothes):
    category_dict = {}
    answer = 1
    for cloth, category in clothes:
        if category not in category_dict:
            category_dict[category] = []
        category_dict[category].append(cloth)
    
    for value in category_dict.values():
        answer *= len(value) + 1
    
    return answer - 1
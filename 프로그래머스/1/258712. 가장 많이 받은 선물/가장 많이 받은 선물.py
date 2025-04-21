from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    answer = 0
    
    # 선물 개수 저장
    gift_dict = defaultdict(lambda: defaultdict(int))
    for gift in gifts:
        f, t = gift.split()
        gift_dict[f][t] += 1
        
    # 선물 지수 계산
    gift_point = defaultdict(int)
    for f in gift_dict:
        for t in gift_dict[f]:
            count = gift_dict[f][t]
            gift_point[f] += count
            gift_point[t] -= count
            
    # 조합 계산
    result_dict = defaultdict(int)
    for x, y in combinations(friends, 2):
        # x가 y에게 선물한 경우
        xy = gift_dict[x][y]
        # y가 x에게 선물한 경우
        yx = gift_dict[y][x]
        
        if xy > yx:
            result_dict[x] += 1
        elif xy < yx:
            result_dict[y] += 1
        else:
            if gift_point[x] > gift_point[y]:
                result_dict[x] += 1
            elif gift_point[x] < gift_point[y]:
                result_dict[y] += 1
    
    answer = max(result_dict.values(), default=0)
    return answer
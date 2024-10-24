def solution(s):
    answer = []
    s = s[2:-2]
    parts = s.split("},{")

    sets = [list(map(int, part.replace(" ", "").split(','))) for part in parts]
    sets.sort(key=len)

    for subset in sets:
        for num in subset:
            if num not in answer:
                answer.append(num)
                break

    return answer
def solution(skill, skill_trees):
    answer = 0
    

    for skill_tree in skill_trees:
        stack = list(skill)
        stack.reverse()
        count = 0
    
        for element in skill_tree:
            if stack and stack[-1] == element:
                stack.pop()
                count += 1
                if count == len(skill):
                    print(skill_tree)
                    answer += 1
                else:
                    continue
    return answer
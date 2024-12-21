def solution(skill, skill_trees):
    answer = 0
    

    for skill_tree in skill_trees:
        tree_stack = list(skill)
        tree_stack.reverse() 
        
        skill_stack = list(skill_tree)
        skill_stack.reverse()
        print(skill_stack)
        for x in range(len(skill_stack) -1, -1, -1):

            if skill_stack[x] in tree_stack:
                if skill_stack[x] == tree_stack[-1]:
                    skill_stack.pop()
                    tree_stack.pop()
                else:
                    # 틀린 경우
                    break
            else:
                skill_stack.pop()
                
            if len(skill_stack) == 0:
                answer += 1
                
        
        
    return answer
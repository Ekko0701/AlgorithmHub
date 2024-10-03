def solution(n, words):
    answer = []
    turn = 0
    already = []
    
    # 가장 처음 원소 추가
    already.append(words[0])
    
    for i in range(1, len(words)):
        # 이미 나온 단어인 경우
        if words[i] in already:
            turn = i
            break
            
        # 끝말 잇기 실패한 경우
        if words[i][0] != words[i - 1][-1]:
            turn = i
            break
            
        already.append(words[i])
        
    # 탈락자
    dropOut = turn % n + 1
    # 탈락자의 탈락 턴
    dropTurn = turn // n + 1
    
    answer = [dropOut, dropTurn]
    if turn == 0:
        answer = [0, 0]
    return answer
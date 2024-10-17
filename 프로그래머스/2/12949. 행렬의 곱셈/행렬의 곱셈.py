def solution(arr1, arr2):
    answer = []
    for m in range(len(arr1)):
        row_array = []
        for r in range(len(arr2[0])):
            element = 0
            for n in range(len(arr2)):
                element += arr1[m][n] * arr2[n][r]
            row_array.append(element)
        answer.append(row_array)
            
    return answer
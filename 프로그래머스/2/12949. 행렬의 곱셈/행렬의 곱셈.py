def solution(arr1, arr2):
    answer = []
    rows_arr1 = len(arr1)
    cols_arr1 = len(arr1[0])
    cols_arr2 = len(arr2[0])
    
    for i in range(rows_arr1):
        result_row = []
        for j in range(cols_arr2):
            sum_value = 0
            for k in range(cols_arr1):
                sum_value += arr1[i][k] * arr2[k][j]
            result_row.append(sum_value)
        answer.append(result_row)
    
    return answer
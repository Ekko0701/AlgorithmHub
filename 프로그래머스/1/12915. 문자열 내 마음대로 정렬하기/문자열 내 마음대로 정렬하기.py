def solution(strings, n):
    var = []
    merge = [0] * len(strings) 
    for i in range(len(strings)):
        var.append(strings[i][n])
        merge[i] = var[i] + strings[i]
    merge.sort()

    for i in range(len(strings)):
        merge[i] = merge[i][1:]

    return merge
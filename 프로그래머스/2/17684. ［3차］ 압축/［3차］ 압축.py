def solution(msg):
    dictionary = {chr(i): i - 64 for i in range(65, 91)}
    dictionary_index = 26
    answer = []
    i = 0

    while i < len(msg):
        w = msg[i]
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary:
                i += 1
                w += msg[i]

        answer.append(dictionary[w])

        if i + 1 < len(msg):
            dictionary_index += 1
            dictionary[w + msg[i + 1]] = dictionary_index
        i += 1

    return answer
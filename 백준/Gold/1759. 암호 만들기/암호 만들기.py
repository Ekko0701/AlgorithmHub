L, C = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()

def backtracking(index, path):
    if len(path) == L:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = sum(1 for char in path if char in vowels)
        consonant_count = len(path) - vowel_count

        if vowel_count >= 1 and consonant_count >= 2:
            print("".join(path))

        return

    for i in range(index, C):
        path.append(alphabets[i])
        backtracking(i + 1, path)
        path.pop()

backtracking(0, [])
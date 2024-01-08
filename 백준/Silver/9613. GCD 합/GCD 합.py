n = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(0, n):
    inputs = list(map(int, input().split()))
    n, numbers, result = inputs[0], inputs[1:], 0
    for x in range(0, n - 1):
        for y in range(x + 1, n):
            result += gcd(numbers[x], numbers[y])
    print(result)
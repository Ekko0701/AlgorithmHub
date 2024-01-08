n, s = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

differences = [abs(x - s) for x in numbers]

result = differences[0]
for diff in differences[1:]:
    result = gcd(result, diff)

print(result)
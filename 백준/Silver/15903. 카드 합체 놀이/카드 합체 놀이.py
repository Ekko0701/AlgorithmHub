n, m = map(int, input().split())
numbers = list(map(int, input().split()))

for i in range(m):
    numbers.sort()
    temp = numbers[0] + numbers[1]
    numbers[0], numbers[1] = temp, temp

print(sum(numbers))
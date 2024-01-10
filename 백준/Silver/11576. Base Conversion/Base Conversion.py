A, B = map(int, input().split())
m = int(input())
numbers = list(map(int, input().split()))
decimal = 0
result = ""

for number in numbers:
    decimal += number * (A ** (m - 1))
    m -= 1
    
while decimal: 
    result = str(decimal % B) + ' ' + result
    decimal = decimal // B

print(result)
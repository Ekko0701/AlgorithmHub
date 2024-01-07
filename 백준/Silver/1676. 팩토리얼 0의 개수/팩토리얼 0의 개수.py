n = int(input())
result = 1

for i in range(n, 1, -1):
    result = result * i

cnt = 0

while result % 10 == 0:
    cnt += 1
    result //= 10

print(cnt)
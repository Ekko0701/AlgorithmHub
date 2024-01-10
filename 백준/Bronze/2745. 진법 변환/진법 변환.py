N, B = input().split()

result,x = 0, 0
count = len(N)
for i in N:
    x = int(i) if i.isnumeric() else ord(i) - 55
    result = result + x * (int(B) ** (count - 1)) 
    count -= 1
print(result)
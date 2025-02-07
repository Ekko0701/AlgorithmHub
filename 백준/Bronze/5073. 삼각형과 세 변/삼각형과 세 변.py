while True:
    numbers = list(map(int, input().split()))
    if numbers == [0, 0, 0]:
        break
    
    if max(numbers) * 2 >= sum(numbers):
        print("Invalid")
    elif len(set(numbers)) == 1:
        print("Equilateral")
    elif len(set(numbers)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
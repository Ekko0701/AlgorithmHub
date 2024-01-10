N, B = map(int, input().split())
result = ""
while (N):
    remain = N % B
    if remain < 10:
        result = str(remain) + result
    else:
        result = chr(remain + 55) + result
    N = N // B

print(result)
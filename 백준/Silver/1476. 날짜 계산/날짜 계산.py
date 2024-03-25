E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
result = 1

while True: 
    if (e == E and s == S and m == M):
        break

    e = e + 1
    s = s + 1
    m = m + 1 
    result += 1
    
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

print(result)
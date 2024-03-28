def caing(m, n, x, y): 
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
        
    return -1

num = int(input())

for _ in range(num):
    m, n, x, y = map(int, input().split())
    print(caing(m, n, x, y))
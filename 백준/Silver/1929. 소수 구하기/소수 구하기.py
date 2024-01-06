import math

M, N = map(int, input().split())

def isPrime(M, N):
    array = [True] * (N + 1)
    for i in range(2, int(math.sqrt(N) + 1)):
        if array[i]: # i가 소수인 경우
            for j in range(i + i, N + 1, i): #i이후 i의 배수들을 False로 바꿈
                array[j] = False
    
    for i in range(M, N+1):
        if i> 1 and array[i] == True:
            print(i)
isPrime(M,N)
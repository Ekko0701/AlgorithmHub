import heapq

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

heapq.heapify(numbers)

for i in range(m):
    temp = heapq.heappop(numbers) + heapq.heappop(numbers)
    heapq.heappush(numbers, temp)
    heapq.heappush(numbers, temp)

print(sum(numbers))
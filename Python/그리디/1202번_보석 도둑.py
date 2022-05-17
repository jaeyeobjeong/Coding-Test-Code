import heapq

n, k = map(int, input().split())

gem_lst, bag_lst = [], []
for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(gem_lst, [w, v])

for _ in range(k):
    bag_lst.append(int(input()))
bag_lst.sort()

answer = 0
tmp = []
for bag in bag_lst:
    while gem_lst and bag >= gem_lst[0][0]:
        heapq.heappush(tmp, -heapq.heappop(gem_lst)[1]) # min heapq이기 때문에, (-) 처리를 해줌. (-99 < -65)
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not gem_lst:
        break

print(answer)
from heapq import heappop, heappush

jobs = [[0, 3], [1, 9], [2, 6]]
def solution(jobs):
    answer = 0
    now, i, start = 0, 0, -1
    heap = []

    while i < len(jobs):
        for w, e in jobs:
            if start < w <= now:
                heappush(heap, (e, w))

        if len(heap) > 0:
            current_e, current_w = heappop(heap)
            start = now
            now += current_e
            answer += now - current_w
            i += 1

        else:
            now += 1

    return answer // len(jobs)

print(solution(jobs))
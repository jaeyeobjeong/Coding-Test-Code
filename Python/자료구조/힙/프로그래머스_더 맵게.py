import heapq
scoville, K = [1,1], 3

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first > K:
            return answer

        mixed = first + second * 2
        answer += 1

        if not scoville:
            if mixed < K:
                return -1
            else:
                return answer
        heapq.heappush(scoville, mixed)

print(solution(scoville, K))
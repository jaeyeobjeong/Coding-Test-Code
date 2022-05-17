from heapq import heappop, heappush

operations = ["I 7","I 5","I -5","D -1"]
def solution(operations):
    answer = []
    for o in operations:
        if "I" in o:
            num = o.split()[1]
            heappush(answer, int(num))
        elif o == 'D -1':
            heappop(answer)
        else:
            # min heap -> max heap
            answer = list(map(lambda x: -x, answer))
            heappop(answer)
            answer = list(map(lambda x: -x, answer))

    return answer

print(solution(operations))
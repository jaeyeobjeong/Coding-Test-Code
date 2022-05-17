from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)  # 현재 다리 위 상황
    truck_weights_ = deque(truck_weights)

    while queue:
        answer += 1

        queue.popleft()

        # truck_weights_를 위에서 pop하지 않는 이유:
        ## weight를 넘어갈 경우에는 truck이 출발하지 말아야하기 때문.
        ## pop은 새 truck이 다리 위로 올라온 것을 의미함.
        if truck_weights_:
            if sum(queue) + truck_weights_[0] <= weight:
                queue.append(truck_weights_.popleft())
            else:
                queue.append(0)

    return answer

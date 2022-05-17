def solution(routes):
    answer = 0
    routes.sort()  # 진입구간이 작은 차량부터 확인
    intersection = []
    while routes:
        start, end = routes.pop(0)
        # 진입구간이 가장 작은 차량 삽입
        if not intersection:
            intersection.append([start, end])
            answer += 1
            continue

        # 새로운 차량과 기존의 차량이 겹치는 구간이 있는지 확인
        inter = False
        for i in range(len(intersection)):
            # 겹치는 구간이 있을 경우에는 겹치는 구간은 새로 설정
            if intersection[i][0] <= start <= intersection[i][1]:
                intersection[i][0] = start
                if end <= intersection[i][1]:
                    intersection[i][1] = end
                inter = True
                break

        # 겹치는 구간이 없을 때는 새로운 카메라 설치가 필요
        if not inter:
            intersection.append([start, end])
            answer += 1

    return answer
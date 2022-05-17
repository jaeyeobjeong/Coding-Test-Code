def solution(n, results):
    answer = 0
    # 선수별 승리, 패배 list 생성
    winner_lst = [set() for _ in range(n + 1)]
    loser_lst = [set() for _ in range(n + 1)]

    for w, l in results:
        winner_lst[w].add(l)
        loser_lst[l].add(w)

    # 기록이 남아있는 경기를 통해 다른 결과를 유추하여 경기 수를 맞춰줌.
    for i in range(1, n + 1):
        # i한테 진 애들은 i를 이긴 애들한테도 진 것
        for winner in winner_lst[i]:
            loser_lst[winner].update(loser_lst[i])
        # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
        for loser in loser_lst[i]:
            winner_lst[loser].update(winner_lst[i])

    for i in range(1, n + 1):
        total_match = len(winner_lst[i]) + len(loser_lst[i])
        if total_match == n - 1:
            answer += 1

    return answer
def sol_1(num):
    ans_lst = [-1, -1, 1, -1, 1, 2, -1, 2, 3, 2]
    if num <= 10:
        return ans_lst[num - 1]

    for i in range(11, num + 1):
        if ans_lst[i - 5 - 1] != -1 and ans_lst[i - 3 - 1] != -1:
            ans_lst.append(min(ans_lst[i - 5 - 1], ans_lst[i - 3 - 1]) + 1)
        elif ans_lst[i - 5 - 1] != -1 and ans_lst[i - 3 - 1] == -1:
            ans_lst.append(ans_lst[i - 5 - 1] + 1)
        elif ans_lst[i - 5 - 1] == -1 and ans_lst[i - 3 - 1] != -1:
            ans_lst.append(ans_lst[i - 3 - 1] + 1)
        else:
            ans_lst.append(-1)
    return ans_lst[-1]

print(sol_1(int(input())))
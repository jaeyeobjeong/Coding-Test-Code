def sol(num):
    ans_lst = [0, 1, 1, 2, 3]
    if num <= 5:
        return ans_lst[num - 1]

    for i in range(6, num + 1):
        if i % 3 == 0 and i % 2 == 0:
            ans_lst.append(min(ans_lst[int(i / 3) - 1], ans_lst[int(i / 2) - 1], ans_lst[i - 1 - 1]) + 1)
        elif i % 3 == 0 and i % 2 != 0:
            ans_lst.append(min(ans_lst[int(i / 3) - 1], ans_lst[i - 1 - 1]) + 1)
        elif i % 3 != 0 and i % 2 == 0:
            ans_lst.append(min(ans_lst[int(i / 2) - 1], ans_lst[i - 1 - 1]) + 1)
        else:
            ans_lst.append(ans_lst[i - 1 - 1] + 1)
    return ans_lst[num - 1]


print(sol(int(input())))
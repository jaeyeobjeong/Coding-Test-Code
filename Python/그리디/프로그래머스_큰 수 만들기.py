def solution(number, k):
    answer = ''
    num_lst = []  # Stack

    for num in number:
        while k > 0 and num_lst and num_lst[-1] < num:
            num_lst.pop()
            k -= 1
        num_lst.append(num)

    for i in range(len(num_lst) - k):
        answer += num_lst[i]

    return answer
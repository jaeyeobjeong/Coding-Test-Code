def sol_2(num):
    lst = [1,0]
    for i in range(num):
        lst.append(sum(lst[-2:]))
    return lst[-2:]

n = int(input())
for i in range(n):
    input_num = int(input())
    answer = sol_2(input_num)
    print(answer[0], answer[1])
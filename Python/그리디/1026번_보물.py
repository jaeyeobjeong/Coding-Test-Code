n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_lst.sort(reverse=True)
b_lst.sort()

result = 0
for a, b in zip(a_lst, b_lst):
    result += a * b

print(result)
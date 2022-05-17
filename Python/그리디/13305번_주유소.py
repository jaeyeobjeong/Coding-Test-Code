n = int(input())
road_lst = list(map(int, input().split()))
store_lst = list(map(int, input().split()))

answer = 0
min_value = 10e9
for i in range(n - 1):
    min_value = min(min_value, store_lst[i])
    answer += road_lst[i] * min_value

print(answer)

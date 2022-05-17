n = int(input())
rgb_lst = [[] for _ in range(n)]
for i in range(n):
    r,g,b = map(int, input().split())
    if i == 0:
        rgb_lst[i] = (r,g,b)
    else:
        rgb_lst[i].append(min(rgb_lst[i - 1][1], rgb_lst[i - 1][2]) + r)
        rgb_lst[i].append(min(rgb_lst[i - 1][0], rgb_lst[i - 1][2]) + g)
        rgb_lst[i].append(min(rgb_lst[i - 1][0], rgb_lst[i - 1][1]) + b)

print(min(rgb_lst[n-1]))
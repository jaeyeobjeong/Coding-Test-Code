a, b = map(int, input().split())

answer = 1
while a < b:
    if (b - 1) % 10 == 0:
        b = (b - 1) / 10
    else:
        b /= 2
    answer += 1

if a != b:
    print(-1)
else:
    print(answer)
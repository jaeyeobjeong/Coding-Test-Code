n = int(input())

dp = [[0] * 10 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = [1] * 10
    else:
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][j:])

print(sum(dp[n - 1]) % 10007)
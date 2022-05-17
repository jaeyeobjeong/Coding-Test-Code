n, k = map(int, input().split())
coin_lst = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k + 1)]

for c in coin_lst:
    if c <= k:
        dp[c] += 1
    for i in range(c, k + 1):
        if i - c > 0:
            dp[i] += dp[i - c]

print(dp)

def solution(money):

    n = len(money)

    dp = [0 for _ in range(n)]
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[2] + money[0]

    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 3]) + money[i]

    max_1 = max(dp[:-1])

    dp = [0 for _ in range(n)]
    dp[0] = 0
    dp[1] = money[1]
    dp[2] = money[2]

    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 3]) + money[i]

    max_2 = max(dp)

    return max(max_1, max_2)
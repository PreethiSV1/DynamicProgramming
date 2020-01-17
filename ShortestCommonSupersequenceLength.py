def ShortestCommonSupersequenceLength(X, m, Y, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    return dp[m][n]


X = "ABCBDAB"
Y = "BDCABA"
print(ShortestCommonSupersequenceLength(X, len(X), Y, len(Y)))
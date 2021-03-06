# Function to find Longest Common Subsequence Length
# eg: ABCDEF, BGDAE ==> 3
def LongestCommonSubsequenceLength(X, m, Y, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[m][n]


X = 'ABBABBA'
Y = 'BABABA'
m = len(X)
n = len(Y)
print(LongestCommonSubsequenceLength(X, m, Y, n))

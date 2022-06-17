
def knapsack(capacity, weight, profits):
    W, n = capacity, len(weight)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for j in range(1, n+1):
        for w in range(1, W+1):
            if weight[j-1] <= w:
                dp[j][w] = max(dp[j-1][w], dp[j-1]
                               [w-weight[j-1]] + profits[j-1])

            else:
                dp[j][w] = dp[j-1][w]

    return dp[n][W], dp


def egg_drop(k, n):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

    """
    Base cases:

    dp[k][1] = 1
    dp[k][0] = 0

    dp[1][n] = n
    dp[0][n] = float("inf")
    """

    for j in range(k+1):
        dp[j][1] = 1

    dp[0] = [float("inf") if i > 0 else 0 for i in range(len(dp[1]))]
    dp[1] = [i for i in range(len(dp[1]))]

    for i in range(2, k+1):
        for j in range(2, n+1):
            dp[i][j] = float("inf")
            for x in range(1, j+1):
                dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x-1], dp[i][j-x]))

    visualize_2d_table(dp)


def edit_distance(self, word1, word2):
    """
        :type word1: str
        :type word2: str
        :rtype: int
        """
    a, b = len(word1), len(word2)
    dp = [[0 for _ in range(a+1)] for _ in range(b+1)]

    for i in range(b+1):
        dp[i][a] = b - i

    for i in range(a+1):
        dp[b][i] = a - i

    for i in range(b-1, -1, -1):
        for j in range(a-1, -1, -1):
            if word1[j] == word2[i]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    return dp[0][0]


def visualize_2d_table(table):
    s = [[str(e) for e in row] for row in table]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


"""
Knapsack Problem
"""
# capacity = 165
# weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
# profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

# visualize_2d_table(knapsack(capacity, weights, profits)[1])


egg_drop(2, 36)

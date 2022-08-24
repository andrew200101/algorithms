
def knapsack(capacity, weight, profits):
    W, n = capacity, len(weight)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for j in range(n):
        for w in range(1, W+1):
            if weight[j] <= w:
                dp[j+1][w] = max(dp[j][w], dp[j]
                                 [w-weight[j]] + profits[j])

            else:
                dp[j+1][w] = dp[j][w]

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

# visualize_2d_table(knapsack(capacity, weights, profits)[1])

# def knapsack_1(capacity, weights, profits):

#     """
#     state = max profit at weight i
#     Take or not to take item i?

#     Take: dp[i] = dp
#     dp[i] =
#     """


# egg_drop(2, 5)

def k2(weights, profits, capacity):
    """
    State dp(i,j) = The maximum  profit at capacity i using weights up to j
    Transition (i,j): we need to determine whether to use item j or not to reach optimal profit given capacity i

                    If we use, then dp(i,j) = dp(i-weights[j],j) + profit[j]
                    What this means is that we are using the best dp val at capacity i-current_weight + the profit of the current item

                    Or we don't use it and simply to dp(i,j) = dp(i, j-1)
    """
    n = len(weights)
    dp = [[0 for _ in range(n+1)] for _ in range(capacity+1)]

    for i in range(1, capacity+1):
        for j in range(n):
            if weights[j] <= capacity:
                dp[i][j+1] = max(dp[i][j], dp[i-weights[j]][j] + profits[j])
            else:
                dp[i][j+1] = dp[i][j]

    return dp[capacity][n]


capacity = 50
weights = [10, 20, 30]
profits = [60, 100, 120]
print(k2(weights, profits, capacity))

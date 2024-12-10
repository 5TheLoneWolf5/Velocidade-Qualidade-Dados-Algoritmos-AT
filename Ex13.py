"""

Esta solução não recursiva do knapsack problem é mais eficiente 

"""

def knapSack(W, wt, val):
        n = len(wt)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
                for w in range(W + 1):
                        if i == 0 or w == 0:
                                dp[i][w] = 0
                        elif wt[i - 1] <= w:
                                dp[i][w] = max(val[i - 1] + dp[i -1][w - wt[i - 1]], dp[i - 1][w])
                        else:
                                dp[i][w] = dp[i - 1][w]

        return dp[n][W]

profit = [5, 5, 10]
weight = [5, 10, 15]
W = 20

print(knapSack(W, weight, profit))

# Resultado: 15.

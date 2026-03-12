'''

'''
def knapsack01(W, val, wt):
    
    # Initializing subtask list, called dp
    # A list of 0s that as long as weight + 1
    # maximum value achievable with weight ≤ w
    dp = [0] * (W + 1)

    # Taking first i elements
    for i in range(1, len(wt) + 1):
        
        # Starting from back, so that we also have data of
        # previous computation of i-1 items
        for j in range(W, wt[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])
    
    return dp[W]

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack01(W, val, wt))

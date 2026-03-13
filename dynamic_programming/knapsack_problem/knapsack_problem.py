'''
This function takes input:
    int maximum knapsack weight capacity, W
    array of the item values, values
    array of the item weights, weights
The function calculates the maximum benefit possible from a given subset while staying under max weight
'''
def knapsack01(W, values, weights):
    
    # Initializing dp subtask list, of Benefits
    # Starts as a list of 0s (as long as max weight + 1)
    # maximum benefit achievable with weight ≤ w
    # benefits[w] = all the maximum benefits achievable keeping weight <= W
    benefits = [0] * (W + 1)

    # Going through all the items
    for item in range(len(weights)):

        # 'item' weight and value
        weight_k = weights[item]
        value_k = values[item]
        
        # "For for w ← W down to w_k do"
        # Start at max weight and go backwards until the current item weight
        for j in range(W, weight_k - 1, -1):
            # For each index from W down to w_k
            # subtract the current item weight to adjust capacity
            if (benefits[j - weight_k] + value_k) > benefits[j]:
                # Take the max
                benefits[j] = benefits[j - weight_k] + value_k

    # The max benefit is at the end of the array
    return benefits[W]

if __name__ == "__main__":
    # items 1, 2, 3, 4
    values = [6, 5, 7, 3]
    weights = [3, 2, 4, 1]
    W = 8

    print("Maximum benefit result: ", knapsack01(W, values, weights))


# Knapsack Problem
Given n objects and a "knapsack."
Item `i` has:
- weight `w_i > 0`
- value (benefit) `b_i > 0`

The knapsack has capacity `W`. Partial items cannot be added to the knapsack.
This algorithm chooses a subset of items whose total weight is ≤ `W` while maximizing total value. 

## Dynamic Programming Idea
**Brute force approach:** would require checking every possible subset of items for the highest total value. Each item in the subset is either `taken` or `left`. These two options are available for all of `n` items, which means would this approach would require checking 2<sup>n</sup> subsets of items.

**Dynamic approach** we store the best value achievable for every weight limit.

An array `benefits[w]` is maintained to represent the maximum benefit achievable with total weight ≤ `W`. This is the core of the dynamic programming approach. The subtask computes a new higher benefit to store in the table with each increasing value for maximum weight, `W`.

The solution is built iteratively by considering items one at a time and updating the table.


## Implementation & Time Cmplexity
The time complexity is **O(n x W)**. 
- The running time is based on two nested `for` loops. 
- The outer loop iterates `n` times and the inner one iterates at most `W` times. 

After the loops the optimal value can be found by locating the value `B[w]` that is greatest among all `w` <= `W`.

## Pseudocode
```text
01Knapsack(S, W):
    Input: Set S of n items, where for each item i ∈ S has positive b_i & w_i
    Output: For w ← 0 ... W, maximum benefit B[w] of a subset of S with total weight ≤ W

    for w ← 0 to W do
        B[w] w ← 0
    for i ← 1 to n do
        for w ← W down to w_k do
            if B[w - w_i] + b_i > B[w] then
                B[w] ← B[w - w_i] + b_i
```

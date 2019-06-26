def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-2], dp[i-1])
    
    return min(dp[-1], dp[-2])


    

ex1 = [10, 15, 20]
ex2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print minCostClimbingStairs(ex1)
print minCostClimbingStairs(ex2)
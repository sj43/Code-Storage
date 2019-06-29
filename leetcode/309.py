def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    A = [0] * len(prices)
    B = [0] * len(prices)
    C = [0] * len(prices)

    A[0] = 0
    B[0] = -prices[0]
    C[0] = float('-inf')

    for i in range(1, len(prices)):
        A[i] = max(A[i-1], C[i-1])
        B[i] = max(B[i-1], A[i-1] - prices[i])
        C[i] = B[i-1] + prices[i]

    return max(A[-1], C[-1])


# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]


print(maxProfit([1,2,3,0,2]))
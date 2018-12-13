# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the
# nth house with kth color, return the minimum cost which achieves this goal.


def buildhouse(matrix):
    num_row = len(matrix)
    num_col = len(matrix[0])
    cache = [[0] * num_col]

    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(cache[r][i] for i in range(num_row) if i != c) + val)
        cache.append(row_cost)
    return min(cache[-1])

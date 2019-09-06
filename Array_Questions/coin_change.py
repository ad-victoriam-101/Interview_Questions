# Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
# how many ways can we make the change? The order of coins doesn’t matter.


# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
# So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
# So the output should be 5.
#values can be reused. 
N = 10
S = [2,5,3,6]
def coin_counter(S,m,n):

    # table[i] will be storing the number of solutions for 
    # value i. We need n+1 rows as the table is constructed 
    # in bottom up manner using the base case (n = 0) 
    # Initialize all table values as 0 
    table = [0 for k in range(n+1)]
    table[0] = 1
    # print(table)
    # Pick all coins one by one and update the table[] values 
    # after the index greater than or equal to the value of the 
    # picked coin 
    for i in range (0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
            print(table)
    return table[n]

print(coin_counter(S,len(S),N))
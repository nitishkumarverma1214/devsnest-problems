def possibleWays(coins,amount:int)->int:

    permutation = [0]*(amount+1)
    permutation[0] =1
    for money in range(len(permutation)):
        for coin in coins:
            if money>=coin:
                permutation[money]+=permutation[money-coin]
    return permutation[amount]


ways = possibleWays([5,2,3,7,6,1,12,11,9,15,16,17,18,19,20],50)
print(ways)
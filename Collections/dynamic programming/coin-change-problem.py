class Solution:
    def __init__(self):
        self.memo = {}
    
    def leastChange(self,coins,amount):
        if amount in self.memo:
            return self.memo[amount]

        if amount ==0:
            return []
        if amount<0:
            return None
        
        leastcoin = None

        for coin in coins:
            change = self.leastChange(coins,amount-coin)
            if change !=None:
                combination =change + [coin]
                if leastcoin==None or len(leastcoin) > len(combination):
                    leastcoin =combination
                   
               
        self.memo[amount] = leastcoin
        return leastcoin

    def coinChange(self, coins, amount: int) -> int:
        change = self.leastChange(coins,amount)
        print(change)
        return len(change) if change!=None else -1
  
obj = Solution()
print(obj.coinChange([1,2,5],11))
print(obj.memo)
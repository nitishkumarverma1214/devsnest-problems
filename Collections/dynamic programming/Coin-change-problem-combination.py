class Solution:
    def change(self, amount: int, coins) -> int:
        combination=[0 for i in range(amount+1)]
        combination[0] =1
       
        for coin in coins:
            for money in range(len(combination)):
                    if money==coin:
                        combination[money] +=1
                    elif money>coin:
                        combination[money] += combination[money-coin] 
            
        print(combination)
       

        return combination[amount]









change = Solution().change(5,[1,2,5])
print(change)
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        memo = {}
        n = len(prices)
        
        def recur(idx, holdingStock,transactionLimit):
            if idx == n or transactionLimit > k:
                return 0
            
            if (idx, holdingStock,transactionLimit) in memo:
                return memo[(idx, holdingStock,transactionLimit)]
            
            dontBuyOrSell = recur(idx + 1, holdingStock,transactionLimit)
            
            if holdingStock:
                sell = prices[idx] + recur(idx + 1, False,transactionLimit)
                result = max(sell, dontBuyOrSell)
            else:
                buy = -prices[idx] + recur(idx + 1, True,transactionLimit+1)
                result = max(buy, dontBuyOrSell)
            
            memo[(idx, holdingStock,transactionLimit)] = result
            return result
        
        return recur(0, False,0)
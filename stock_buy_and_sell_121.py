# Brute force:: You are given an array prices where prices[i] is the price of a given stock on the ith day.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        for i in range(0, n):
            bought=prices[i]
            for j in range(i+1, n):
                sold=prices[j]
                if sold-bought>profit:
                    profit = sold-bought
        return profit

  #Optimal Solution
  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float("inf")
        profit=0
        for i in range(0,len(prices)):
            if min_price>prices[i]:  
                min_price=prices[i]
            difference=prices[i]-min_price
            if difference>profit:
                profit=difference
        return profit

from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

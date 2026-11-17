class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        budget = money
        bought = 0
        for price in prices:
            if price <= money:
                bought += 1
                money -= price

            if bought == 2:
                return money
        return budget
            
        
class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        frees = [0] * n

        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            frees[i] = cnt

        dp = [0] * (budget + 1)

        for i in range(n):
            _, cost = items[i]
            bonus = 1 + frees[i]
            for b in range(budget, cost - 1, -1):
                if dp[b - cost] + bonus > dp[b]:
                    dp[b] = dp[b - cost] + bonus

            for b in range(cost, budget + 1):
                if dp[b - cost] + 1 > dp[b]:
                    dp[b] = dp[b - cost] + 1

        return dp[budget]
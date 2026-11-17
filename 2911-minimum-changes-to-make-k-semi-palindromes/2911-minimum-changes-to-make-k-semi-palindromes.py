
class Solution:
    def minimumChanges(self, s, k) :
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):

 
            divisors = []

            for d in range(1, length):
                if length % d == 0:
                    divisors.append(d)

            for start in range(n - length + 1):
                best = float('inf')

                for d in divisors:
                    changes = 0

                  
                    for r in range(d):
                        left = start + r
                        right = start + length - d + r

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[start][start + length - 1] = best

        dp = [[float('inf')] * (k + 1)
              for _ in range(n + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):

                for t in range(2 * (parts - 1), i - 1):

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[t][parts - 1] +
                        cost[t][i - 1]
                    )

        return dp[n][k]

from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = 10**9

        left = [INF] * n
        cur_sum = 0
        l = 0
        best = INF

        for r in range(n):
            cur_sum += arr[r]

            while cur_sum > target:
                cur_sum -= arr[l]
                l += 1

            if cur_sum == target:
                best = min(best, r - l + 1)

            left[r] = best
        right = [INF] * n
        cur_sum = 0
        r = n - 1
        best = INF

        for l in range(n - 1, -1, -1):
            cur_sum += arr[l]

            while cur_sum > target:
                cur_sum -= arr[r]
                r -= 1

            if cur_sum == target:
                best = min(best, r - l + 1)

            right[l] = best

        ans = INF

        for i in range(n - 1):
            if left[i] != INF and right[i + 1] != INF:
                ans = min(ans, left[i] + right[i + 1])

        return -1 if ans == INF else ans
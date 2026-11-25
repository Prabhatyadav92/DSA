from collections import Counter


class Solution(object):

    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        # Base larger than max(nums) (max nums[i] <= 10^5)
        B1, M1 = 100003, 1000000007
        B2, M2 = 100019, 1000000009

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i in range(n):
            val = nums[i]
            p1[i + 1] = (p1[i] * B1) % M1
            p2[i + 1] = (p2[i] * B2) % M2
            pref1[i + 1] = (pref1[i] * B1 + val) % M1
            pref2[i + 1] = (pref2[i] * B2 + val) % M2

        def get_hash(l, r):
            # Subarray nums[l:r] of length k = r - l
            k = r - l
            h1 = (pref1[r] - pref1[l] * p1[k]) % M1
            h2 = (pref2[r] - pref2[l] * p2[k]) % M2
            return (h1, h2)

        def has_unique_of_len(length):
            counts = Counter()
            for i in range(n - length + 1):
                counts[get_hash(i, i + length)] += 1
            return any(cnt == 1 for cnt in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
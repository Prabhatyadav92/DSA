class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        max_len = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                val = nums[j]
                prod *= val
                g = val if g == 0 else gcd(g, val)
                l = lcm(l, val)

                if prod == l * g:
                    max_len = max(max_len, j - i + 1)

        return max_len
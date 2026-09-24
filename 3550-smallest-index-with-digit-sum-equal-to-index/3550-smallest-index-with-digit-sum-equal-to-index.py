class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            sum1 = 0

            while val > 0:
                sum1 += val % 10
                val //= 10

            if i == sum1:
                return i

        return -1
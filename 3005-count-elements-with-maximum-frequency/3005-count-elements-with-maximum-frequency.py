from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)

        max_freq = max(freq.values())

        return sum(f for f in freq.values() if f == max_freq)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        max_str = {}
        left = 0
        right = 0
        n = len(s)

        while right < n:
            if s[right] in max_str:
                left = max(left, max_str[s[right]] + 1)

            max_str[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
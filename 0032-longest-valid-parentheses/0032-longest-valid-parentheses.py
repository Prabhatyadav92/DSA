class Solution(object):
    def longestValidParentheses(self, s):
        op = 0
        cl = 0
        ans = 0

        for ch in s:
            if ch == "(":
                op += 1
            else:
                cl += 1

            if op == cl:
                ans = max(ans, 2 * cl)

            elif cl > op:
                op = 0
                cl = 0
        op = 0
        cl = 0

        for ch in reversed(s):
            if ch == "(":
                op += 1
            else:
                cl += 1

            if op == cl:
                ans = max(ans, 2 * op)

            elif op > cl:
                op = 0
                cl = 0

        return ans
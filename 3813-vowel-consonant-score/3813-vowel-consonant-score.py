class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        count = 0
        vc = 0

        for ch in s:
            if ch in "aeiou":
                count += 1
            elif ch.isalpha():
                vc += 1

        if vc == 0:
            return 0

        return count // vc
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = {}

        # Count frequency of each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        res = []
        seen = set()

        for ch in s:
            count[ch] -= 1

            if ch in seen:
                continue

            # Remove bigger characters if they appear again
            while res and res[-1] > ch and count[res[-1]] > 0:
                removed = res.pop()
                seen.remove(removed)

            res.append(ch)
            seen.add(ch)

        return "".join(res)
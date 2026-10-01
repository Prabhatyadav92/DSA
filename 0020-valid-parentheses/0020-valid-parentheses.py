class Solution:
    def isValid(self, s: str) -> bool:
        seen={
            ")":"(",
            "}":"{",
            "]":"["

        }
        nset=[]

        for ch in s:
            if ch in seen:
                if not nset or nset[-1] != seen[ch]:
                    return False
                nset.pop()
            else:
                nset.append(ch)
        return len(nset)==0




        
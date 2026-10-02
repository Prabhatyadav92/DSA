class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def bc(s, open ,close):
            if open==n and close==n:
                res.append(s)
                return
            if open<n:
                bc(s + "(", open + 1, close)
            if close<open:
                bc(s + ")", open, close + 1)
        bc("",0,0)
        return res







        
        
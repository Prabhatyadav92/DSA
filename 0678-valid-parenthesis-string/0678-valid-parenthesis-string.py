class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ct=0
        pt=0
        for ch in s:
            if ch=="(":
                ct+=1
                pt+=1
            elif (ch==")"):
                pt-=1
                ct-=1
            else:
                pt-=1
                ct+=1
            pt=max(0,pt)

            if ct<0:
                return False
        return pt==0
        
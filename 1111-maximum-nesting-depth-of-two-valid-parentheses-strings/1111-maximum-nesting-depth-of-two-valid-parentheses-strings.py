class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ls=[]
        count=0
        for ch in seq:
            if ch=="(":
                count+=1
                ls.append(count%2)
            else:
                ls.append(count%2)
                count -=1
        return ls
        
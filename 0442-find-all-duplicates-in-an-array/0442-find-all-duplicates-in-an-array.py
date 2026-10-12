class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans={}
        res=[]
        for num in nums:
            if num  in ans:
                res.append(num)
            else:
                ans[num]=True

               
        return res

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        ac_sum=n*(n+1)//2
        giv_sum=sum(nums)
        return ac_sum - giv_sum
        
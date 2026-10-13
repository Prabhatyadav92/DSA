class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key =lambda x: x*x)
        n=len(nums)
        mid=n//2
        sm=sum(x*x for x in nums[:mid])
        lg=sum(x*x for x in nums[mid:])
        return lg-sm
           
            


        
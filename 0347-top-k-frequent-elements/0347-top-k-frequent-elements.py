class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count=Counter(nums)
        arr=sorted(count.items(),key=lambda x:x[1],reverse=True)
        return[num for num,freq in arr[:k]]
  
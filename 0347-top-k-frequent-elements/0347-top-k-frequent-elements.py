# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         # count=Counter(nums)
#         # arr=sorted(count.items(),key=lambda x:x[1],reverse=True)
#         # return[num for num,freq in arr[:k]]

from collections import Counter
# from typing import List
class Solution:
    def topKFrequent(self,nums,k):
        freq=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        res=[]
        for count in range(len(nums),0,-1):
            for num in buckets[count]:
                res.append(num)
                if len(res)==k:
                    return res
        return res


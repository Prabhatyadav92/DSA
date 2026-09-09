class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p_map={}
        n=len(nums)
        for i in range(n):
            diff=target-nums[i]
            if diff in p_map:
                return [p_map[diff],i]
            p_map[nums[i]]=i

        return

        
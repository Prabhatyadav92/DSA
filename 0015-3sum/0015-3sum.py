class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for a in range(len(nums) - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            left = a + 1
            right = len(nums) - 1

            while left < right:

                total = nums[a] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    ans.append([nums[a], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans
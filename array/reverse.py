def rev(nums, left, right):
    if left >= right:
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    return rev(nums, left+1, right-1)

nums = [1, 2, 3, 4, 5]
print(rev(nums, 0, len(nums)-1))
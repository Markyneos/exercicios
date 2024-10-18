class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int | None:
    if len(nums) == 1:
      if target > nums[0]:
        return 1
      else:
        return 0
    if target < nums[0]:
      return 0
    for i in range(len(nums)):
      if nums[i] == target:
        return i
      elif target > nums[i - 1] and target < nums[i + 1]:
        return i
    if target > nums[-1]:
      return len(nums)





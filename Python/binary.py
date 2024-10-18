class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    mid = end // 2
    while True:
      if target == nums[mid]:
        return mid
      elif target > nums[mid]:
        start = mid
        mid = start + end // 2
      elif target < nums[mid]:
        end = mid
        mid = start + end // 2
      if target > nums[mid] and target < nums[mid + 1]:
        return mid + 1
      if target < nums[mid] and target > nums[mid - 1]:
        return mid - 1


nums = [1, 3, 5, 6]
target = 2
objeto = Solution()
print(objeto.searchInsert(nums, target))

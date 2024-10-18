class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
      mid = (start + end) // 2
      if nums[mid] < target:
        start = mid + 1
      elif nums[mid] > target:
        end = mid - 1
      else:
        return mid
    return start

nums = [1, 3, 5, 6]
target = 7
objeto = Solution()
print(objeto.searchInsert(nums, target))

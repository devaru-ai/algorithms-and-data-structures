# Two Sum II

# 1-indexed array
# array in non-decreasing order
# sol must use only constant extra space
# hint: use two pointers

from typing import List
class Solution:
  def twoSumm(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    l = 0
    r = n - 1
    
    while l < r:
      summ = nums[l] + nums[r]
      if summ == target:
        return [l+1, r+1]
      elif summ > target:
        r -= 1
      else:
        l += 1

nums = [2, 7, 10, 22]
target = 9
solution_instance = Solution()
result = solution_instance.twoSumm(nums, target)
print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {result}")
      




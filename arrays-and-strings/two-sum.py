# Two Sum
# Input: nums = [2, 7, 11, 15], Target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] == 9, return [0, 1]

from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}
    for i, n in enumerate(nums):
      diff = target - n
      if diff in prevMap:
        return [prevMap[diff], i]
      prevMap[n] = i
    return

nums = [2, 2, 3, 15]
target = 5
solution_instance = Solution()
result = solution_instance.twoSum(nums, target)
print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {result}")

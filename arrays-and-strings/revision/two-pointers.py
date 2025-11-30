# Valid Palindrome (Easy) – Do you know how to move pointers inward?
def isPalindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    if not s[left].isalnum():
      left += 1
    elif not s[right].isalnum():
      right -= 1
    elif s[left].lower() != s[right].lower():
      return False
    else:
      left += 1
      right -= 1
  return True
  
# Two Sum II - Input Array Is Sorted (Medium) – The classic sorted array optimization.
# Given an array of integers, nums, and an integer target, return the indices of the two numbers such that they add up to target.

def twoSum(numbers: List[int], target: int) -> List[int]:
  left = 0
  right = len(numbers) - 1
  while left < right:
    curr_sum = numbers[left] + numbers[right]
    if curr_sum == target:
      return [left+1, right+1]
    elif curr_sum > target:
      right -= 1
    else:
      left += 1
  return []
  
# 3Sum (Medium) – Handles duplicates and triplet logic.
# Given an integer array nums, return all the triplets [a, b, c] such that a + b + c = $.

def threeSum(nums: List[int]) -> List[List[int]]:
  res = []
  nums.sort()
  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    left = i + 1
    right = len(nums) - 1
    while left < right:
      total = nums[i] + nums[left] + nums[right]
      if total < 0:
        left += 1
      elif total > 0:
        right -= 1
      else:
        res.append([nums[i], nums[left], nums[right]])
        left += 1
        while left < right and nums[left] == nums[left - 1]:
          left += 1
      return res
# Container With Most Water (Medium) – Teaches "greedy" pointer movement (deciding which side to shrink).
def maxArea(height: List[int]) -> int:
  left = 0
  right = len(height) - 1
  max_water = 0
  while left < right:
    width = right - left
    curr_height = min(height[left], height[right])
    curr_area = width * curr_height
    max_water = max(max_water, curr_area)
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1
  return max_water

      
# Trapping Rain Water (Hard) – Combines pre-computation or two-pointers with complex logic.

  
# Move Zeroes (Easy) – In-place manipulation (read/write pointers).
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Constraint: You must do this in-place without making a copy of the array.
def moveZeroes(nums: List[int]) -> None:
  slow = 0
  for fast in range(len(nums)):
    if nums[fast] != 0:
      nums[slow], nums[fast] = nums[fast], nums[slow]
      slow += 1








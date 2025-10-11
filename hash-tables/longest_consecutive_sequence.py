from typing import List
class Solution:
  def longestConsecutiveSeq(self, nums: List[int]) -> int:
    longest = 0
    s = set(nums)
    
    for num in nums:
      if num - 1 not in s:
        next_num = num + 1
        len = 1
        while next_num in s:
          len += 1
          next_num += 1
          
        longest = max(longest, len)
    return longest

nums = [1,2,3,4,880,889,90]
sol = Solution()
res = sol.longestConsecutiveSeq(nums)
print(f" Output: {res}")

from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n
    for i in range(n):
      j = -i - 1
      l_arr[i] = l_mult
      r_arr[j] = r_mult
      l_mult *= nums[i]
      r_mult *= nums[j]
    return [l*r for l, r in zip(l_arr, r_arr)]

array = [1,3,0,9]
sol_instance = Solution()
result = sol_instance.productExceptSelf(array)
print(f" Input: {array}")
print(f" Output: {result}")

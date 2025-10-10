from collections import Counter
from typing import List

class Solution:
  def topKFreq(self, nums: List[int], k: int) -> List[List[int]]:
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n+1)
    
    for num, freq in counter.items():
      if buckets[freq] == 0:
        buckets[freq] = [num]
      else:
        buckets[freq].append(num)
        
    ret = []
    for i in range(n, -1, -1):
      if buckets[i] != 0:
        ret.extend(buckets[i])
      if len(ret) == k:
        break
    return ret

nums = [1, 2, 2, 3, 3, 3]
k = 2
sol = Solution()
res = sol.topKFreq(nums, k)
print(f" Output: {res}")
      

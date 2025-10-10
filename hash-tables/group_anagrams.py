from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams_dict = defaultdict(list)
    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord('a')] += 1
      key = tuple(count)
      anagrams_dict[key].append(s)
    return anagrams_dict.values()

strs = ["nat", "ant", "cat", "bat"]
sol = Solution()
result = sol.groupAnagrams(strs)
print(f" Input: {strs}")
print(f" Output: {result}")
    

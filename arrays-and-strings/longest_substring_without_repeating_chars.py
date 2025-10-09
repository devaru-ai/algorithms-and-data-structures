# Longest Substring Without Repeating Characters

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    longest = 0
    sett = set()
    n = len(s)
    
    for r in range(n):
      while s[r] in sett:          # invalid substring
        sett.remove(s[r])
        l += 1
      w = (r - l) + 1
      longest = max(longest, w)
      sett.add(s[r])
      
    return longest

s = "abcbacbb"
sol_instance = Solution()
result = sol_instance.lengthOfLongestSubstring(s)
print(f"Input: {s}")
print(f"Output: {result}")




    

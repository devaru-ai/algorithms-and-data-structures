class Solution:
  def charReplacement(self, s: str, k: int) -> int:
    l = 0
    longest = 0
    n = len(s)
    counts = [0] * 26
    
    for r in range(n):
      counts[ord(s[r]) - 65] += 1
      while (l-r+1) - max(counts) > k:
        counts[ord(s[r]) - 65] -= 1
        l += 1
      longest = max(longest, (r-l+1))
                    
    return longest

s = "AABAACBB"
k = 2
sol_instance = Solution()
result = sol_instance.charReplacement(s, k)
print(f"Input: s = {s}, k = {k}")
print(f"Output: {result}")

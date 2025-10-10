from collections import Counter
class Solution:
  def validAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict == t_dict

str1 = "anagram"
str2 = "nagrama"
sol_instance = Solution()
result = sol_instance.validAnagram(str1, str2)
print(f" Input: string 1 = {str1}, string 2 = {str2}")
print(f" Output: {result}")

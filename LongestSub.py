
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        result = 0

        for right,ele in enumerate(s):
            if ele in dic:
                left = max(left , dic[ele]+1)
            dic[ele] = right
            result = max(result , right - left + 1)
        return result

a = "pwwkew"

s = Solution()
x = s.lengthOfLongestSubstring(a)
print(x)
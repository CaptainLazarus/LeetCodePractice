from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr1 = Counter(s1)
        i = 0
        while i < len(s2) - len(s1) + 1:
            if s2[i] in ctr1:
                ctr2 = Counter(s2[i:i+len(s1)])
                if ctr1 == ctr2:
                    return True
            i+=1
        return False
        


a = "ab"
# b ="eidbaooo"
b = "eidboaoo"

a = "bbbbbbbbbbbbbbbbbbbbbb"
b = "bbbbbbbbbbbbbbbbbbbbbbcb"

s = Solution()
x = s.checkInclusion(a,b)
print(x)
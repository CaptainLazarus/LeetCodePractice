from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        dic ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        output = []
        for i,e in enumerate(s):
            output.append(int(dic[e]))
        
        sum = 0
        for i in range(len(output)-1):
            if output[i] >= output[i+1]:
                sum += output[i]
            else:
                sum -= output[i]
        sum += output[len(output)-1]
        return sum

# Solution 2. Funnily enough, this actually ran slower than the previous one.

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dic ={
#             "I":1,
#             "V":5,
#             "X":10,
#             "L":50,
#             "C":100,
#             "D":500,
#             "M":1000
#         }
#         sum = 0
#         for i in range(len(s)-1):
            
#             if dic[s[i]] >= dic[s[i+1]]:
#                 sum = sum + dic[s[i]]
#             else:
#                 sum = sum - dic[s[i]]
#         sum += dic[s[len(s)-1]]
#         return sum


a = "DCDXXIX"

s = Solution()
print(s.romanToInt(a))
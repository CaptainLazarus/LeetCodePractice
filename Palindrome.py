class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x >= 0 and x <= 9:
            return True
        elif x >= 10:
            sum = 0
            r = 0
            q = 0
            target = x
            while x > 10:
                q = x//10
                r = x%10
                sum = sum*10 + r
                x = x//10
            if sum == target:
                return True
            else:
                return False

a = 121

s = Solution()
print(s.isPalindrome(a))
import math

class Solution:

	def checkTriplet(self,arr, n):
		if n <= 2:
			return False
			
		new_arr = [x*x for x in arr]
		new_arr.sort()
		
		for i in range(n-1 , 1 , -1):
			start = 0
			end = i-1
		
			while start < end:
				a = new_arr[start]
				b = new_arr[end]
				c = new_arr[i]
				if a + b == c:
					return True
				else:
					if a + b > c:
						end -= 1
					elif a + b < c:
						start += 1
		
		return False

nums = [93, 39, 80, 91, 58, 59, 92, 16, 89, 57, 12, 3, 35, 73, 56, 29, 47, 63, 87]
nums = [39 , 80 , 89]
n = len(nums)

s = Solution()
output = s.checkTriplet(nums , n)
print(output)
class Solution:

    def findMinDiff(self, arr , n , m):
        arr.sort()
        min_diff = arr[n-1] - arr[0]
        
        for i in range((n-m)):
            min_diff = min(min_diff , arr[i + m - 1] - arr[i])
        return min_diff

nums  = [34, 88, 89, 39, 67, 71, 85, 57, 18, 7, 61, 50, 38, 6, 60, 18, 19, 46, 84, 74, 59]
m = 12

s = Solution()
output = s.findMinDiff(nums , len(nums) , m)
print(output)
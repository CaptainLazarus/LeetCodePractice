class Solution:    
    def maxSubArraySum(self,arr):
        ##Your code here
        local_max = 0
        global_max = -100000001
        start = 0
        end = 0
        
        for i in range(len(arr)):
            # local_max = max(arr[i] , arr[i] + local_max)
            if arr[i] > (arr[i] + local_max):
                start = end = i
                local_max = arr[i]
            elif arr[i] < (arr[i] + local_max):
                local_max = arr[i] + local_max
                if arr[i] >= 0:
                    end = i
            else:
                end = i
                local_max = arr[i] + local_max
            if local_max > global_max:
                global_max = local_max
        return [global_max , arr[start:end+1]]

nums = [-1,1,3,-4,9,2,-5 , -5, 10]

s = Solution()
output = s.maxSubArraySum(nums)
print(output)
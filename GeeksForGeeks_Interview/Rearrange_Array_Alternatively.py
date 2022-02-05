class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        p1 = 0
        p2 = n-1
        output = []
        flag = True
        for i in range(n):
            if flag:
                output.append(arr[p2])
                flag = False
                p2-=1
            else:
                output.append(arr[p1])
                flag = True
                p1+=1
        
        for i in range(n):
            arr[i] = output[i]
        return arr
 
nums = [1,3,4,5,6,7]
n = len(nums)

s = Solution()
output = s.rearrange(nums , n)
print(output)
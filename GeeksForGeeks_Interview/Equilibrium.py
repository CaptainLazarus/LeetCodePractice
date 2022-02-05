# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if N==1:
            return 1
        elif N==2:
            return -1
        else:
            sum_arr = [0]*N
            reversed_sum_arr = [0]*N
            
            sum_arr[0] = A[0]
            reversed_sum_arr[N-1] = A[N-1]
            
            for i in range(1,len(A)):
                sum_arr[i] = sum_arr[i-1] + A[i]
                reversed_sum_arr[N-i-1] = reversed_sum_arr[N-i] + A[N-i-1]
            
            # print(sum_arr)
            # print(reversed_sum_arr)
            
            index = -1
            for i in range(1,len(A)):
                if sum_arr[i] == reversed_sum_arr[i]:
                    index = i+1
                
            return index

nums = [1,3,5,2,2]
nums = [-1,1,3,-4,9,2,-5,-5,10]

s = Solution()
output = s.equilibriumPoint(nums , len(nums))
print(output)
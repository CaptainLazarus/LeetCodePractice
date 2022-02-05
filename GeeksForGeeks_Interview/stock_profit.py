
class Solution:
    #Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self , arr, n):
        if n == 1:
            return []
        
        buy_index = 0
        sell_index = 0

        output = []
        i=0
        while i < n-1:
            a = arr[i+1]
            b = arr[i]
            while (i < n-1) and arr[i+1] <= arr[i]:
                a = arr[i]
                b = arr[i-1] 
                i+=1
            
            if (i == n-1):
                break
            
            buy = i
            i+=1

            a = arr[i]
            b = arr[i-1]    
            while (i < n) and arr[i] >= arr[i-1]:
                a = arr[i]
                b = arr[i-1] 
                i+=1
            
            sell = i-1
            output.append((buy , sell))
        return output
                

nums = [10, 5, 7, 1, 4, 3]
nums = [100, 180, 260, 310, 40, 535, 695]
nums = [11, 42, 49, 96, 23, 20, 49, 26, 26, 18, 73, 2, 53, 59, 34, 99, 25, 2]
n = len(nums)

s = Solution()
output = s.stockBuySell(nums,n)
print(output)
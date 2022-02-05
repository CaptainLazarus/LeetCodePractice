import math


class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        # code here
    count = N//K
    for i in range(count):
        temp = list(reversed(arr[(i*K): (i+1)*K]))
        for j in range(K):
            arr[j + (i*K)] = temp[j]

    temp = list(reversed(arr[(N//K * K): N]))
    for j in range(N % K):
        arr[j + (N//K * K)] = temp[j]
    return arr
# {
#  Driver Code Starts
# Initial template for Python


def main():
    T = int(input())
    while(T > 0):
        nk = [int(x) for x in input().strip().split()]
        N = nk[0]
        K = nk[1]
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        ob.reverseInGroups(arr, N, K)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()

class Solution:
    def frequencyCount(self, arr, N, P):
        f = {}
        ans = []
        for i in range(N):
            if arr[i] in f:
                f[arr[i]] += 1
            else:
                f[arr[i]] = 1
                
        for i in range(1, N+1):
            if i in f:
                arr[i-1] = f[i]
            else:
                arr[i-1] = 0

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1
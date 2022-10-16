
from typing import List
class Solution:
    def count(self, n : int, s : str) -> List[str]:
        ansS = ''
        ansD = 0
        ans = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                ans += 1
            else:
                ans += 1
                if ansD < ans:
                    ansD = ans
                    ansS = s[i]
                ans = 0
        ans += 1
        if ansD < ans:
            ansD = ans
            ansS = s[-1]
        return [ansS, ansD]
                    
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i)
    

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        s = (input())
        
        obj = Solution()
        res = obj.count(n, s)
        
        StringArray().Print(res)
        

from unicodedata import digit


def digitSum(n, ans):
    if n < 10:
        ans += n
        return ans
    ans += n%10
    return digitSum(n//10, ans)
n = int(input())
print(digitSum(n , 0))
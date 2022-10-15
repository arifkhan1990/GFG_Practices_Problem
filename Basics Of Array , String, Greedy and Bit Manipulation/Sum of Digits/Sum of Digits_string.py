def digitSum(s):
    ans = 0
    for i in s:
        ans += int(i)
    return ans
n = input()
print(digitSum(n))
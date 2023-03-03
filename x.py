from collections import Counter
def nth(t,n,d):
    return t + (d*n) - d

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    cl = [(ar[i] - ar[i-1]) for i in range(1,n)]
    c = Counter(cl).most_common(1)
    d = 0
    print(c)
    ans = 0
    p = ((n-1)*d) - ar[-1] 
    if p != ar[0]:
        ar[0] = p
    for i in range(n):
        p = nth(ar[0], i+1, d)
        # print(p)
        if p != ar[i]:
            ans += 1
        if ans > 1:
            break
    print('NO' if d == 0 or ans > 1 else 'YES')

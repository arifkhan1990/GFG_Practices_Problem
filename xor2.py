import math
 
n , k = map(int, input().split( ))
ar = list(map(int, input().split( )))
#size of the block and the number of blocks
len = int(math.sqrt (n + .0) + 1) 
b = [0]*n
a = []

for i in range(n):
    if i==0:
        a.append(ar[i])
    else:
        x = a[-1] ^ ar[i]
        a.append(x)

# for i in range(n):
#     b[i // len] += a[i]
# print(a,b)

for _ in range(k):
#     ans = 0
#     #answering the queries
    l,r = map(int, input().split( ))
    print(sum(a[l:r]))
#     #read input data for the next query
#     b1, b2 = l//len, r//len
#     p , q = ((l//len)+1)*len - 1, (r//len)*len

#     if b1 == b2:
#         for i in range(l,r+1):
#             ans += a[i]
#     else:
#         for i in range(l,p+1):
#             ans += a[i]

#         for i in range(b1+1, b2):
#             ans += b[i]

#         for i in range(q,r+1):
#             ans += a[i]
#     print(ans)
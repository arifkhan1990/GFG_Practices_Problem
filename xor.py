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

for i in range(n):
    b[i // len] += a[i]
print(a,b)

for _ in range(k):
    ans = []
    #answering the queries
    l,r = map(int, input().split( ))
    #read input data for the next query
    sum = 0
    for i in range(l,r+1):
        if i < n:
            if (i % len == 0 and i + len - 1 <= r):
                #if the whole block starting at i belongs to [l, r]
                sum += b[i // len]
                i += len
            else :
                sum += ar[i]
                i += 1
        else:
            break
    print(sum)
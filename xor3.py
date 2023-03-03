from sys import stdin
ip = stdin.readline
from itertools import combinations, accumulate
n , k = map(int, ip().split( ))
ar = list(map(int, ip().split( )))
b = []
id = []
for i in range(n-1):
    id.append(len(b))
    b.append(ar[i])
    for j in range(i+1, n):
         b.append(b[-1]^ar[j]) 
# print(b,id)
for _ in range(k):
    p,q = map(int, ip().split( ))
    p,q = p-1, q
    print(sum(b[id[p]:id[p] + q - p]))
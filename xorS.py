from sys import stdin
ip = stdin.readline


def xorSum(arr, n):
 
    bits = 0
 
    # Finding bitwise OR of all elements
    for i in range(n):
        bits |= arr[i]
        print(bits)
    ans = bits * pow(2, n-1)
 
    return ans



n , k = map(int, ip().split( ))
ar = list(map(int, ip().split( )))
# print(b,id)
for _ in range(k):
    p,q = map(int, ip().split( ))
    p,q = p-1, q
    print(xorSum(ar[p:q], len(ar[p:q])))
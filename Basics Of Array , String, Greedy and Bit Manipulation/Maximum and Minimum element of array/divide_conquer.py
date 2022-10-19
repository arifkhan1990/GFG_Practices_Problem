def maxAndmin(ar, low, high):
    if low == high:
        return (ar[low], ar[high])
    elif high == low + 1:
        if ar[low] > ar[high]:
            return (ar[high], ar[low])
        else:
            return (ar[low], ar[high])
    else:
        md = (low+high)//2
        mn1,mx1 = maxAndmin(ar,low,md)
        mn2,mx2 = maxAndmin(ar,md+1,high)
        return (min(mn1,mn2), max(mx1,mx2))

for _ in range(int(input())):
    ar = list(map(int,input().split()))
    mn , mx = maxAndmin(ar,0,len(ar)-1)
    print(mn,mx)
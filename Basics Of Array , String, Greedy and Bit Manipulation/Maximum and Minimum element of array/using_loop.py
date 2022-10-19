for _ in range(int(input())):
    ar = list(map(int,input().split()))
    mn, mx = float('inf'), 0
    for i in ar:
        mx = max(mx, i)
        mn = min(mn, i)
    print(mn, mx)
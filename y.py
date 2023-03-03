for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))

    s, di = 0, 0
    if n < 3:
        if (n == 2):
            di = ar[1] - ar[0]
            s = ar[0] - di
        elif((ar[1] - ar[0]) == ar[2] - ar[1]):
            s = ar[0]
            di = ar[1] - ar[0]
    else:
        if (n == 3):
            di = ar[2] - ar[1]
            s = ar[1] - di
        elif((ar[1] - ar[0]) == ar[2] - ar[1]):
            s = ar[0]
            di = ar[1] - ar[0]
        elif ((ar[2] - ar[1]) == (ar[3] - ar[2])):
            di = ar[2] - ar[1]
            s = ar[1] - di
        else:
            di = (ar[3] - ar[0]) / 3
            s = ar[0]

    new_ar = []
    ans = 0
    for i in range(n):
        p = int(s+(i * di))
        # print(p,ar[i])
        if ar[i] != p:
            ans += 1
        if ans > 1:
            break
    #     new_ar.append()
    # b = [(new_ar[i] - new_ar[i-1]) for i in range(1,n)]
    # print(ans)
    print('NO' if ar[-1] == 0 or ans > 1 else "YES")
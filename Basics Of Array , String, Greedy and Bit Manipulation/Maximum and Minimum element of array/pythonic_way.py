for _ in range(int(input())):
    ar = list(map(int,input().split()))
    ar.sort()
    print(ar[0],ar[-1])
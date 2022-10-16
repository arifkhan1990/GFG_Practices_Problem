from sys import stdin
ip = stdin.readline

def sum1(ar):
    if len(ar) == 1:
        return ar[0]
    else:
        return ar[0] + sum1(ar[1:])
for _ in range(int(ip())):
    ar = list(map(int, ip().split()))
    print(sum(ar))
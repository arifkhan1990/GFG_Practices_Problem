from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    ar = list(map(int, ip().split()))
    print(sum(ar))
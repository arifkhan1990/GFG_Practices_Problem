for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split(' ')))
    li = li[::-1]
    print(*li)
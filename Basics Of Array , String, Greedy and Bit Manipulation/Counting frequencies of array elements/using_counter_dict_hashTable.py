from collections import Counter
for _ in range(int(input())):
    ar = list(map(int,input().split()))
    count = Counter(ar)
    for i in count.keys():
        print(i, count[i])

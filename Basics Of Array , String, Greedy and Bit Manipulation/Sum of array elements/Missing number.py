def missingNumber( A, n):
     return (n*(n+1) // 2) - sum(A)

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1

if __name__ == "__main__":
    main()
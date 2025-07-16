def recursion(b, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return recursion(b, n/2) * recursion(b, n/2)
    else:
        return b * recursion(b, n-1)


print(recursion(map(int, input().split())))

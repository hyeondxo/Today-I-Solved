import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

a.sort()


def binary_search(target):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == target:
            return 1
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


for target in x:
    print(binary_search(target))

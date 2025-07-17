import sys
input = sys.stdin.readline


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


n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()

x = list(map(int, input().split()))
for target in x:
    print(binary_search(target))

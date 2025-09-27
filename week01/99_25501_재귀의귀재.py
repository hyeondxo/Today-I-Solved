import sys
input = sys.stdin.readline


def recursion(str, left, right):
    global count
    count += 1
    if left >= right:
        return 1
    elif str[left] != str[right]:
        return 0

    return recursion(str, left + 1, right - 1)


def isPalindrome(str):
    return recursion(str, 0, len(str) - 1)


n = int(input())

for i in range(n):  # ?
    global count
    count = 0

    print(f"{isPalindrome(input().strip())} {count}")
    print("test")

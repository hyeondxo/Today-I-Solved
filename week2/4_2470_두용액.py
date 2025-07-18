import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

find_left = 0
find_right = 0
min_value = float('inf')


def update_min(new_val, left, right):
    global find_left, find_right, min_value
    abs_new_var = abs(new_val)
    if abs_new_var < min_value:
        min_value = abs_new_var
        find_left = arr[left]
        find_right = arr[right]
    return


def binary_search():
    global find_left, find_right
    left = 0
    right = n - 1

    while left < right:
        new_val = arr[left] + arr[right]
        if new_val == 0:
            find_left, find_right = arr[left], arr[right]
            return
        elif new_val < 0:
            update_min(new_val, left, right)
            left += 1
        else:
            update_min(new_val, left, right)
            right -= 1
    return


binary_search()
print(find_left, find_right)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()


def calculate_sum(height):
    sum = 0
    for tree in trees:
        cut_height = tree - height
        sum += cut_height if cut_height >= 0 else 0
    return sum


def binary_search():
    left = 0
    right = max(trees)
    while left <= right:
        mid = (left + right) // 2
        cur_sum = calculate_sum(mid)
        if cur_sum == m:
            return mid
        if cur_sum < m:
            right = mid - 1
        else:
            left = mid + 1

    return right


print(binary_search())

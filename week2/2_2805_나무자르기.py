import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

# start = 0
# end = max(trees)
# 잘랐을 때 나온 나무의 합을 M과 비교하며 이분 탐색


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
        if cur_sum < m:  # 작으니 더 잘라야 함 -> m왼쪽으로 이동 ->
            right = mid - 1
        else:
            left = mid + 1

    return right  # 정확한 답을 못 찾고 while문이 끝나더라도 최소 높이 조건을 만족하는 마지막 값


print(binary_search())

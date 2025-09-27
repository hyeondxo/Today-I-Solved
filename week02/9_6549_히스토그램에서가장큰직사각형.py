import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def solve(start, end):
    if start == end:
        return heights[start]
    mid = (start + end) // 2
    left_max = solve(start, mid)
    right_max = solve(mid + 1, end)
    mid_max = calculate_mid(start, end, mid)

    return max(left_max, right_max, mid_max)


def calculate_mid(start, end, mid):
    left = mid
    right = mid + 1
    height = min(heights[left], heights[right])
    max_area = height * 2
    while start < left or right < end:
        if right < end and (left == start or heights[right + 1] >= heights[left - 1]):
            right += 1
            height = min(height, heights[right])
        else:
            left -= 1
            height = min(height, heights[left])
        max_area = max(max_area, height * (right - left + 1))

    return max_area


while True:
    n, *heights = list(map(int, input().split()))
    if n == 0:
        break
    print(solve(0, n-1))

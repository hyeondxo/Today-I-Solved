import math
import sys
input = sys.stdin.readline

n = int(input())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))
pos.sort()


def calculate_mid(start, end, mid, temp_min):
    nears = []
    for i in range(start, end+1):
        if (pos[mid][0]-pos[i][0])**2 <= temp_min:
            nears.append(pos[i])

    nears.sort(key=lambda x: x[1])
    min_distance = temp_min
    for i in range(0, len(nears)):
        near_1 = nears[i]
        for j in range(i+1, len(nears)):
            near_2 = nears[j]
            if min_distance <= (near_1[1]-near_2[1])**2:
                break
            near_distance = (near_1[0]-near_2[0])**2 + (near_1[1]-near_2[1])**2
            min_distance = min(min_distance, near_distance)

    return min_distance


def solve(left, right):
    if right == left:
        return 10 ** 9
    if right - left == 1:  # 두 점만 남았을 때 두 점의 길이를 반환
        return (pos[right][0]-pos[left][0])**2 + (pos[right][1]-pos[left][1])**2

    mid = (left + right) // 2
    left_min = solve(left, mid)
    right_min = solve(mid+1, right)
    temp = left_min if left_min < right_min else right_min
    mid_min = calculate_mid(left, right, mid, temp)

    return mid_min


print(solve(0, n-1))

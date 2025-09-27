import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
arr = list(map(int, input().split()))
total_count = 0
# 사대의 위치 리스트를 정렬한다
arr.sort()


def binary_search(x, y):
    left = 0
    right = m - 1
    min_distance = float('inf')
    while left <= right:
        mid = (left + right) // 2

        # 만약 현재 사대로부터의 거리가 더 짧으면 사대를 갱신한다
        cur_distance = abs(arr[mid] - x) + y
        if cur_distance < min_distance:
            min_distance = cur_distance

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return min_distance


for i in range(n):
    x, y = map(int, input().split())
    # 각 동물에 대해 가장 가까운 사대의 위치를 찾는다

    # 가장 가까운 사대로부터의 거리가 L 이하이면 카운트를 증가한다
    if binary_search(x, y) <= l:
        total_count += 1

# 최종 카운트를 출력한다
print(total_count)

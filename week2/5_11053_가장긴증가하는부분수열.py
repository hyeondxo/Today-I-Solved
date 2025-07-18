import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
result = []  # result 배열의 길이만큼의 수열 중에서 가장 작은 값들로만 유지


def binary_search(target):
    left = 0
    right = len(result) - 1

    while left <= right:
        mid = (left + right) // 2
        if result[mid] == target:
            return mid
        if result[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


for number in a:
    if len(result) == 0:
        result.append(number)
        continue

    max_val = result[-1]
    if number > max_val:
        result.append(number)
    else:
        # result는 길이별로 가장 작은 끝값을 유지하는 배열이므로,
        # 현재 값 number가 들어가야 할 위치를 찾아 기존 값을 더 작은 값으로 교체하여,
        # 해당 길이의 증가 부분 수열 끝값을 최적화함 (더 긴 수열 확장 가능성 확보)
        index = binary_search(number)
        result[index] = number

print(len(result))

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = []  # result 배열의 길이만큼의 수열 중에서 가장 작은 값들로만 유지
pos = [0] * n
prev_index = [-1] * n
index_map = []


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


for i in range(n):
    number = a[i]

    index = binary_search(number)
    if index == len(result):
        result.append(number)
        index_map.append(i)
    else:
        result[index] = number
        index_map[index] = i

    pos[i] = index
    if index > 0:
        prev_index[i] = index_map[index - 1]


lis_length = len(result)

lis = []
last_index = index_map[-1]

for i in range(n-1, -1, -1):
    if pos[i] == lis_length - 1:
        last_index = i
        break

while last_index != -1:
    lis.append(a[last_index])
    last_index = prev_index[last_index]

lis.reverse()

print(lis_length)
sys.stdout.write(" ".join(map(str, lis)))

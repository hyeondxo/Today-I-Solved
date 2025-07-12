import sys

arr = list(map(int, sys.stdin.read().splitlines()))
# arr = [int(x) for x in sys.stdin.readlines()]

index, max_num = max(enumerate(arr), key=lambda x: x[1])

print(max_num)
print(index + 1)

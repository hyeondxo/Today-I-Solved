import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
fruit = defaultdict(int)
arr = list(map(int, input().split()))
left = 0
max_count = 0

for right in range(n):
    fruit[arr[right]] += 1

    while len(fruit) > 2:
        fruit[arr[left]] -= 1
        if fruit[arr[left]] == 0:
            del fruit[arr[left]]
        left += 1

    max_count = max(max_count, right - left + 1)

print(max_count)

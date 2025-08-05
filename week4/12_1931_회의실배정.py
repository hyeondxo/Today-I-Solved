import sys
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: (x[1], x[0]))

total_count = 0
last_end = 0
for start, end in times:
    if start >= last_end:
        total_count += 1
        last_end = end

print(total_count)

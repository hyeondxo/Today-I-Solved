import sys
input = sys.stdin.readline

width, height = map(int, input().split())
n = int(input())

vertical = [0]
horizontal = [0]

for i in range(n):
    is_vertical, number = map(int, input().split())
    if is_vertical:
        vertical.append(number)
    else:
        horizontal.append(number)

vertical.append(width)  # 0, 4, 10
horizontal.append(height)  # 0, 3, 2, 8

vertical.sort()
horizontal.sort()

sizes = []
for i in range(1, len(vertical)):
    for j in range(1, len(horizontal)):
        w = vertical[i] - vertical[i - 1]
        h = horizontal[j] - horizontal[j - 1]
        sizes.append(w * h)

print(max(sizes))

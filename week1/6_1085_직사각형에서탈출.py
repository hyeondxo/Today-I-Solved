import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

output = min(x, y, h - y, w - x)

sys.stdout.write(str(output) + "\n")

import math
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

up_day = (v - a) / (a - b)

print(math.ceil(up_day + 1))

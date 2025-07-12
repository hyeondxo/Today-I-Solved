import sys
input = sys.stdin.readline

n = int(input())

max = 10001
count = [0] * max

for i in range(1, n + 1):
    number = int(input())
    count[number] += 1

for i in range(1, max):
    is_valid_number = count[i]
    if is_valid_number:
        for _ in range(is_valid_number):
            print(i)

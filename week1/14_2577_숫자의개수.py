import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
num = a * b * c

output = [0 for _ in range(10)]

for i in str(num):
    output[int(i)] += 1

for total_count in output:
    print(total_count)

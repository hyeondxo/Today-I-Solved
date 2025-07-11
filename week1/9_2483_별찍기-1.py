import sys
input = sys.stdin.readline
output = []

n = int(input())

for i in range(n):
    output.append("*" * (i + 1))

sys.stdout.write("\n".join(output))

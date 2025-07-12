import sys
input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    r, s = input().split()
    output.append("".join(x * int(r) for x in s))

sys.stdout.write("\n".join(output))

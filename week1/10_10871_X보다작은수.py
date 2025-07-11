import sys
input = sys.stdin.readline

n, x = map(int, input().split())
output = [num for num in input().split() if int(num) < x]

sys.stdout.write(" ".join(output))

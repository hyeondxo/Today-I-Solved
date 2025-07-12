import sys
input = sys.stdin.read

data = input().split()
n, *numbers = list(map(int, data))
numbers.sort()
sys.stdout.write("\n".join(str(number) for number in numbers))

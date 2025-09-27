import sys
input = sys.stdin.readline

expression = input().strip()

parts = expression.split('-')
first_sum = sum(map(int, parts[0].split('+')))
sub_sum = sum(sum(map(int, part.split('+'))) for part in parts[1:])

print(first_sum - sub_sum)

import sys
input = sys.stdin.readline

year = int(input())

output = 0

cond_1 = year % 400
cond_2 = year % 4
cond_3 = year % 100

if cond_1 == 0:
    output = 1
elif cond_2 == 0 and cond_3 != 0:
    output = 1

sys.stdout.write(str(output))

import sys
input = sys.stdin.readline


def is_hansu(num):
    digits = list(map(int, num))
    return digits[0] - digits[1] == digits[1] - digits[2]


n = int(input())

if (n < 100):
    print(n)
    sys.exit()
elif n < 111:
    print(99)
    sys.exit()

count = 99
for i in range(111, n+1):
    if is_hansu(str(i)):
        count += 1

print(count)

import sys
input = sys.stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            return False
    return True


input()

output = [num for num in input().split() if is_prime(int(num))]
print(len(output))

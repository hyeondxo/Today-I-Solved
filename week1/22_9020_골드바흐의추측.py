import sys
input = sys.stdin.readline


def is_prime(n):
    if (n < 2):
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            return False

    return True


t = int(input())
for _ in range(t):
    n = int(input())
    half = int(n / 2)
    num1 = half
    num2 = half
    for i in range(1, half + 1):
        if is_prime(num1) and is_prime(num2):
            print(num1, num2)
            break

        num1 = half - i
        num2 = half + i

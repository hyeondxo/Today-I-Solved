n = int(input())

numbers = [int(input()) for _ in range(n)]
for i in sorted(numbers):
    print(i)

n = int(input())


def solve(y):
    global count
    if y == n:
        count += 1

    for x in range(n):
        if check_x[x] == 0 and check_up_right[y + x] == 0 and check_down_right[y - x] == 0:
            check_x[x] = 1
            check_up_right[y + x] = 1
            check_down_right[y - x] = 1
            solve(y + 1)
            check_x[x] = 0
            check_up_right[y + x] = 0
            check_down_right[y - x] = 0


count = 0
check_x = [0 for _ in range(n)]
check_up_right = [0 for _ in range(2 * n - 1)]
check_down_right = [0 for _ in range(2 * n - 1)]


solve(0)
print(count)
print(count)

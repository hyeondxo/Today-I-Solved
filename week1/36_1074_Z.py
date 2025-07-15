n, row, col = map(int, input().split())


def solve(n, row, col):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    size = half * half

    if row < half and col < half:
        return solve(n - 1, row, col)
    if row < half and col >= half:
        return size + solve(n - 1, row, col - half)
    if row >= half and col < half:
        return size * 2 + solve(n - 1, row - half, col)
    if row >= half and col >= half:
        return size * 3 + solve(n - 1, row - half, col - half)


print(solve(n, row, col))

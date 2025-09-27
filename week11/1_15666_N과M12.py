import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
path = []
result = []

def backtrack(start, depth):
    if depth == m:
        result.append(" ".join(map(str, path)))
        return

    last_num = 0  # 같은 depth에서 중복 방지
    for i in range(start, n):
        if last_num != nums[i]:  # 같은 수를 중복해서 시작하지 않음
            path.append(nums[i])
            backtrack(i, depth + 1)  # i부터 시작 (중복 허용)
            path.pop()
            last_num = nums[i]

backtrack(0, 0)
print("\n".join(result))
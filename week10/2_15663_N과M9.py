import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
visited = [False] * n
path = []
result = []

def dfs(depth):
    if depth == m:
        result.append(" ".join(map(str, path)))
        return
    
    last_num = 0
    for i in range(n):
        if not visited[i] and last_num != nums[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(depth + 1)
            path.pop()
            visited[i] = False
            last_num = nums[i]

dfs(0)
print("\n".join(result))

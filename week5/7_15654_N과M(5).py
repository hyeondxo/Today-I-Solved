import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() 

used = [False] * N
path = [0] * M
out_lines = []

def dfs(depth: int):
    if depth == M:
        out_lines.append(" ".join(map(str, path)))
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            path[depth] = arr[i]
            dfs(depth + 1)
            used[i] = False

dfs(0)
sys.stdout.write("\n".join(out_lines))

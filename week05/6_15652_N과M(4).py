import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []
out_lines = []

def dfs(next_start):
    if len(path) == M:
        out_lines.append(" ".join(map(str, path)))
        return
    
    for x in range(next_start, N+1):
        path.append(x)
        dfs(x)   
        path.pop()     

dfs(1)
sys.stdout.write("\n".join(out_lines))

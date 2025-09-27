from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
move = {}  

for _ in range(n+m):
    a, b = map(int, input().split())
    move[a] = b

visited = [False] * 101
dist = [0] * 101 

queue = deque([1])
visited[1] = True

while queue:
    cur = queue.popleft()
    if cur == 100:
        print(dist[cur])
        break

    # 주사위 1~6 굴리기
    for dice in range(1, 7):
        nxt = cur + dice
        if nxt > 100:
            continue
        # 사다리나 뱀 있으면 이동
        if nxt in move:
            nxt = move[nxt]
        if not visited[nxt]:
            visited[nxt] = True
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)
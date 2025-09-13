from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, target):
    visited = [False] * 10000
    queue = deque()
    queue.append((start, ""))  
    visited[start] = True

    while queue:
        num, path = queue.popleft()
        if num == target:
            return path

        next = (num * 2) % 10000
        if not visited[next]:
            visited[next] = True
            queue.append((next, path + "D"))

        next = (num - 1) % 10000
        if not visited[next]:
            visited[next] = True
            queue.append((next, path + "S"))

        next = (num % 1000) * 10 + (num // 1000)
        if not visited[next]:
            visited[next] = True
            queue.append((next, path + "L"))

        next = (num % 10) * 1000 + (num // 10)
        if not visited[next]:
            visited[next] = True
            queue.append((next, path + "R"))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))
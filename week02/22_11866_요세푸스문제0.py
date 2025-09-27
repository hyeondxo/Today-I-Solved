from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(i+1 for i in range(n))
eliminated = []

while queue:
    for i in range(k-1):
        if not queue:
            break
        queue.append(queue.popleft())
    eliminated.append(queue.popleft())

sys.stdout.write("<" + ", ".join(map(str, eliminated)) + ">")

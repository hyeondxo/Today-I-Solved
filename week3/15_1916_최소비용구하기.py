import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [float('inf')] * (n + 1)

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())


def dijkstra(start):
    min_heap = []
    distance[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        dist, now = heapq.heappop(min_heap)
        if distance[now] < dist:
            continue
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(min_heap, (new_cost, next_node))


dijkstra(start)
print(distance[end])

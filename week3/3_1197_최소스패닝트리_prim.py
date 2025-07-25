import heapq
import sys
input = sys.stdin.readline

# 정점, 간선 입력
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

# 비용 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False for _ in range(v+1)]
min_heap = []
heapq.heappush(min_heap, (0, 1))  # 초기 비용 0, 시작 노드 1

total_cost = 0

while min_heap:  # 최소 힙이 빌 때까지 반복
    cost, node = heapq.heappop(min_heap)  # 가장 적은 비용의 노드 pop
    if visited[node]:  # 방문한 노드라면 다음으로
        continue
    visited[node] = True  # 방문 처리
    total_cost += cost  # 비용 합산

    for next_cost, next_node in graph[node]:  # 해당 노드와 연결된 모든 노드들 순회
        if visited[next_node]:  # 방문한 노드라면 다음으로
            continue
        heapq.heappush(min_heap, (next_cost, next_node))  # 최소 힙에 push

print(total_cost)

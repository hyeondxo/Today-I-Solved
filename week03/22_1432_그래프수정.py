import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)] # 역방향 그래프
outdegree = [0] * n # 진출 차수 (나가는 간선 수)

for i in range(n):
    line = input().strip()
    for j, is_link in enumerate(line):
        if is_link == "1":
            graph[j].append(i) # 진출 노드에 현재 들어오는 노드의 정보를 저장
            outdegree[i] += 1 # 진출 차수 증가

result = [0] * n
def topological_sort():
    max_heap = []
    for node in range(n):
        if outdegree[node] == 0:
            heapq.heappush(max_heap, -node) # 진출차수 0을 최대 힙으로 저장 (가장 숫자가 커야하는 곳)
    
    cur_max = n
    while max_heap:
        last_node = -heapq.heappop(max_heap) # 현재의 가장 마지막 노드를 pop
        result[last_node] = cur_max # 결과 배열의 노드 인덱스를 현재의 최대 숫자로 설정
        cur_max -= 1 # 최대 숫자 -1

        for prev_node in graph[last_node]: # 현재 노드로 들어오는 노드들을 검사
            outdegree[prev_node] -= 1 # 이전 노드의 진출 차수를 감소
            if outdegree[prev_node] == 0: # 진출 차수가 0이라면 마지막 노드인 것
                heapq.heappush(max_heap, -prev_node)

topological_sort()
is_cyclic = False
for i in result:
    if i == 0: # 결과 배열에 하나라도 번호가 할당되지 않았다면 사이클이 생긴 것 -> 큐에 들어가지 못했기 때문
        is_cyclic = True
        break

if is_cyclic:
    print(-1)
else:
    print(*result)
    
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
indegree = [0] * (n+1)
part = [[0] * (n+1) for _ in range(n+1)] # part[a][b] = 제품 a를 만들기 위해 b가 몇 개 필요한 지를 저장
for _ in range(m):
    x, y, k = map(int, input().split()) # 5 1 2일 때
    graph[y].append((x, k)) # 1은 5를 만들기 위해 2개가 필요함을 저장
    indegree[x] += 1 # 1 -> 5의 방향이므로 5의 진입 차수 +1

def topological_sort():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0: # 즉시 만들 수 있는 부품들
            queue.append(i)
            part[i][i] = 1 # 이 부품을 만들기 위해서는 자기 자신만 있으면 됨
    
    while queue:
        cur_part = queue.popleft() # 현재 만들 수 있는 부품
        for next_part, need_count in graph[cur_part]: # 현재 부품으로 만들고자 하는 상위 부품, 그 부품을 만들기 위한 갯수
            for default_part in range(1, n+1):
                # 상위 부품의 기본 부품 필요 갯수 = 현재 부품의 기본 부품 필요 갯수 * 현재 부품 자체의 필요 갯수
                part[next_part][default_part] += part[cur_part][default_part] * need_count
            
            indegree[next_part] -= 1
            if indegree[next_part] == 0: # 해당 상위 부품을 만들 준비가 된 것
                queue.append(next_part)

topological_sort()
for i in range(1, n+1):
    total_count = part[n][i]
    if total_count > 0:
        print(i, total_count)

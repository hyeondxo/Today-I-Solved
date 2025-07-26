import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
edges = []
# 1. 노드(정점, v)와 간선(e) 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 2. 비용 정보 오름차순 정렬
edges.sort()
# 3. 부모 테이블 초기화
parent = [i for i in range(v+1)]

total_min_cost = 0
# 간선 정보 하나씩 확인하며 크루스칼 알고리즘 수행
for cost, a, b in edges:
    # find 연산 후, 부모노드가 다르면 사이클이 발생하지 않은 것이므로 union 연산 수행 후 최소 신장 트리에 포함
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_min_cost += cost

print(total_min_cost)

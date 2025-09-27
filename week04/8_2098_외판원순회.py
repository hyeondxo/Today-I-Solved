import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# dp[현재도시][방문상태]
# 현재 도시(cur)에서 'visited' 상태로 방문한 도시들이 정해져 있을 때
# 아직 방문하지 않은 도시들을 모두 방문하고 0번 도시로 돌아가는 최소 비용을 저장
dp = [[-1] * (1 << n) for _ in range(n)]
# 도시가 4개(0, 1, 2, 3)일 때:
# 	•	1. dp[0][0001] →
# 	•	현재 0번 도시, 방문 상태 = 0001 (0만 방문)
# 	•	남은 도시 = 3개 (1, 2, 3)
# 	•	결과: 0번에서 시작해 1, 2, 3을 모두 방문 후 다시 0으로 가는 최소 비용
#	•	2. dp[1][0011] →
#	•	현재 1번 도시, 방문 상태 = 0011 (0, 1 방문)
#	•	남은 도시 = 2개 (2, 3)
#	•	결과: 1번에서 2와 3을 모두 방문 후 0으로 돌아가는 최소 비용
#	    3. dp[2][0111] →
#	•	현재 2번 도시, 방문 상태 = 0111 (0, 1, 2 방문)
#	•	남은 도시 = 1개 (3)
#	•	결과: 2번에서 3번 방문 후 0으로 돌아가는 최소 비용

def tsp(cur, visited):
    # (1) 모든 도시 방문 완료 체크
    if visited == (1 << n) - 1:
        # 현재 도시에서 시작 도시(0)로 돌아가는 길이 있다면 비용 반환, 없다면 무한대
        return w[cur][0] if w[cur][0] > 0 else float("inf") 
    
    # (2) 메모이제이션: 이미 계산된 상태라면 재사용
    if dp[cur][visited] != -1: 
        return dp[cur][visited]
    
    # (3) 현재 상태에서 최소 비용을 구하기 위해 초기값을 무한대로 설정
    cost = float('inf')
    
    # (4) 다음 도시 탐색
    for next in range(n): 
        # 아직 방문하지 않았고, 현재 도시에서 다음 도시로 가는 경로가 존재한다면
        if not (visited & (1 << next)) and w[cur][next] > 0:
            # 방문 상태를 갱신 (현재 visited에 next 도시 방문 표시 추가)
            next_visited = visited | (1 << next) 
            # 재귀의 요정 - 다음 도시에서 남은 도시 방문 후 0으로 돌아가는 최소 비용 계산
            next_cost = tsp(next, next_visited) 
            # 현재 도시에서 다음 도시로 가는 비용 + 이후 경로 비용
            new_cost = w[cur][next] + next_cost 
            # 최소 비용 갱신
            cost = min(cost, new_cost) 
    
    # (5) 현재 상태에서 계산된 최소 비용을 DP 테이블에 저장
    dp[cur][visited] = cost 
    return cost

# 시작 도시를 0으로, 방문 상태는 0번 도시만 방문한 상태(0001)
print(tsp(0, 1))
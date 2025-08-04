import sys
input = sys.stdin.readline

n, m = map(int, input().split())
smalls = [int(input()) for _ in range(m)]
init = float('inf')
# max_speed = n # 메모리초과
max_speed = int((2*n)**0.5) + 1 # 속도 최대값의 근사치(상수를 버린 근의 공식의 근사)
# max_speed = int((1 + (1 + 8*n)**0.5) / 2) + 1  # 정확한 근의공식 기반 최대값 계산
dp = [[init]*(max_speed+1) for _ in range(n+1)] # dp[i][k] : i번째 돌에 k의 속도로 도착했을 때 최소 점프 횟수 / 직전 상태에서 한 번 점프하여 현재 상태로 온 최소 횟수
# 현재 점프 속도가 k라면, 다음 점프 속도는 k+-1 까지만 가능하기 때문에
# 단순히 돌의 위치만 저장하면 안되고, 현재 속도도 함께 저장해야 다음 상태를 정확히 계산 가능
dp[1][0] = 0 # 첫 위치는 1번 돌이고 첫 속도는 0이고 점프 횟수는 0
dp[2][1] = 1

for stone in range(2, n+1): # 2번 돌부터 모든 돌을 확인
    if stone in smalls: # 작은 돌이라면 건너뜀
        continue
    limit_speed = int((2*stone)**0.5)+1 # 현재 돌의 위치에서 가능한 속도의 최댓값
    for speed in range(1, limit_speed):
        if dp[stone][speed] == init: # 이속도로 도달한 적 없는 돌은 건너뜀(경로가 없었단 뜻이므로)
            continue
        for next_speed in [speed-1, speed, speed+1]:
            if next_speed < 1 or next_speed > max_speed: # 유효 속도 검증
                continue
            next_stone = stone + next_speed 
            if next_stone <= n and next_stone not in smalls:# 다음 돌의 위치 검증
                dp[next_stone][next_speed] = min(dp[next_stone][next_speed], dp[stone][speed] + 1) # 최소 점프 수 으로 갱신

min_count = min(dp[n])
print(min_count if min_count != init else -1)
        
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[False] * n for _ in range(n)]
for _ in range(k):  # 사과 입력
    y, x = map(int, input().split())
    board[y-1][x-1] = True
l = int(input())

direction_time = deque()
for _ in range(l):  # 시간, 방향 정보 입력
    time, dir = input().split()
    direction_time.append((int(time), dir))

# 우, 하, 좌, 상 / L : idx-1, R : idx+1
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 뱀 이동 계산 : snake popleft + direction[i] -> snake append
time = 0
snake = deque([[0, 0, 0]])  # 초기 : y = 0, x = 0, direction = 0


def update_direction():
    # 4. 게임이 시작한지 X초라면 snake[0]의 위치에 D 혹은 L을 기록
    if not direction_time:
        return
    if time == direction_time[0][0]:
        if direction_time[0][1] == "L":
            snake[0][2] = (snake[0][2] - 1) % 4
        else:
            snake[0][2] = (snake[0][2] + 1) % 4
        direction_time.popleft()


while True:
    # 0. while True -> time 카운트 += 1
    time += 1
    # 1. 모든 snake의 좌표+방향을 통해 뱀 이동
    head_y, head_x, dir_idx = snake[0]
    ny = head_y + direction[dir_idx][0]
    nx = head_x + direction[dir_idx][1]
    # 2. snake[0] + direction[i](머리) 확인    # 좌표 범위 밖으로 벗어나면 카운트 출력 후 게임 종료
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        print(time)
        sys.exit()

    # 3. 충돌 확인 -> 머리의 좌표가 다른좌표들과 하나라도 겹친다면 카운트 출력 후 게임 종료
    if len(snake) > 1:
        for cur_snake in list(snake)[1:]:
            if cur_snake[0] == ny and cur_snake[1] == nx:
                print(time)
                sys.exit()

    # 뱀 이동
    snake.appendleft([ny, nx, dir_idx])

    if board[ny][nx] == True:  # 사과 먹기
        board[ny][nx] = False
        update_direction()
        continue
    else:
        snake.pop()

    update_direction()

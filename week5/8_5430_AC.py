from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    x = input().strip().strip("[]")
    if x:
        x_arr = list(map(int, x.split(",")))
    else:
        x_arr = []
    dq = deque(x_arr)

    is_left = True
    is_error = False
    for command in p:
        if command == "R":
            is_left = True if not is_left else False
        else: # D일 경우
            if len(dq) == 0: # 삭제할 원소가 없을 경우
                is_error = True
                break
            else:
                if is_left:
                    dq.popleft()
                else:
                    dq.pop()
    if is_error:
        print("error")
    else:
        if is_left:
            print("[" + ",".join(map(str, dq)) + "]")
        else:
            print("[" + ",".join(map(str, reversed(dq))) + "]")

# Core logic
# 기본적으로 popleft
# 뒤집으면 pop

import sys
input = sys.stdin.readline

n = int(input())
pos = []

for _ in range(n):
    x, half = map(int, input().split())
    pos.append((x - half, "("))
    pos.append((x + half, ")"))
pos.sort(key=lambda x: (x[0], 0 if x[1] == ")" else 1))

stack = []
count = 1
for i in range(2 * n):
    cur_bracket = pos[i]
    if stack:
        top = stack[-1]
        if cur_bracket[1] == "(":
            if top[0] < cur_bracket[0]:
                if pos[i-1][0] < cur_bracket[0]:  # 바로 직전 x값보다도 클 경우 (끊어짐)
                    stack[-1] = (top[0], top[1], False)  # 이전 원도 접하지 않음 처리
                stack.append(
                    (cur_bracket[0], cur_bracket[1], False))  # 접해있지 않음
            else:
                stack[-1] = (top[0], top[1], True)  # 이전 원도 접함 처리
                # 얘는 아직 모름
                stack.append((cur_bracket[0], cur_bracket[1], False))
        else:  # ")"
            # 이전 원이 계속 접해왔고, 좌표, 괄호가 같다면
            if top[2]:
                if pos[i-1][0] == cur_bracket[0]:
                    count += 2  # 영역 1개 더 증가
                else:
                    count += 1
                stack.pop()
            else:
                stack.pop()
                count += 1
    else:
        stack.append((cur_bracket[0], cur_bracket[1], False))

print(count)

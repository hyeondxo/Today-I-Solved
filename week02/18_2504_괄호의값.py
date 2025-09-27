import sys
input = sys.stdin.readline

input = input().strip()
result = []


def invalid_string():
    print(0)
    sys.exit()


def find_until_close(find, val):
    if not result:
        invalid_string()
    temp = 0
    while result:
        top = result.pop()
        if top == find:
            # 여는 괄호 발견 → 누적값 처리 후 종료
            # 안쪽에 값이 없으면 기본 값만 추가
            # 값이 있으면 누적값 * 괄호값
            result.append(val if temp == 0 else temp * val)
            return
        elif isinstance(top, int):
            # 괄호 안에서 발견된 숫자는 temp에 누적
            temp += top
        else:
            # 닫는 괄호를 처리중인데 잘못된 여는 괄호가 발견됨
            invalid_string()
    # 반복문 끝나고도 여는 괄호를 못찾았으면 잘못된 입력임
    invalid_string()


for command in input:
    if command == "(":
        result.append("(")
    elif command == "[":
        result.append("[")
    elif command == ")":
        find_until_close("(", 2)
    elif command == "]":
        find_until_close("[", 3)
    else:
        invalid_string()

for v in result:  # 결과 스택에는 숫자만 남아있어야 함
    if not isinstance(v, int):
        invalid_string()

print(sum(result))

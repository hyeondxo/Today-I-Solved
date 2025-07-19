import math
import sys
input = sys.stdin.readline

str = input().strip()
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
            if temp == 0:
                result.append(val)
            else:
                result.append(temp * val)
            break
        elif isinstance(top, int):
            temp += top
        else:
            invalid_string()


for command in str:
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

for v in result:
    if not isinstance(v, int):
        invalid_string()
print(sum(result))

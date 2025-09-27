from collections import deque
import sys
input = sys.stdin.readline

t = int(input())


def is_vps(line):
    stack = deque()
    for s in line:
        if s == "(":
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    return True


for _ in range(t):
    line = input().strip()
    if is_vps(line):
        print("YES")
    else:
        print("NO")

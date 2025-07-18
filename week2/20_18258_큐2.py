import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()


def action_command(command, val):
    if val:
        queue.append(val)
    elif command == "front":
        if not queue:
            print(-1)
            return
        print(queue[0])
    elif command == "back":
        if not queue:
            print(-1)
            return
        print(queue[-1])
    elif command == "pop":
        if not queue:
            print(-1)
            return
        print(queue.popleft())
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)


for _ in range(n):
    val = ""
    line = input().split()
    if len(line) == 2:
        command, val = line[0], line[1]
    else:
        command = line[0]

    action_command(command, val)

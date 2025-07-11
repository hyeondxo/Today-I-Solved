import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    line = input().strip()
    score = 0
    total_score = 0

    for result in line:
        if result == "O":
            score += 1
            total_score += score
        else:
            score = 0

    print(total_score)

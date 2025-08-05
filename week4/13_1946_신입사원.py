import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(n)]
    scores.sort(key= lambda x: x[0])
    min_interview = scores[0][1]
    count = 1
    for document, interview in scores:
        # 여기서 나오는 애들은 min_intervie 보다 작은지만 보면 됨
        if interview < min_interview:
            count += 1
            min_interview = interview
    print(count)

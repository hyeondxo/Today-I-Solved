import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operstors = []
o = ["+", "-", "*", "//"]
for i, cnt in enumerate(list(map(int, input().split()))):
    for _ in range(cnt):
        operstors.append(o[i])

visited = [False for _ in range(len(operstors))]

max_result = float('-inf')
min_result = float('inf')


def dfs(result, depth):
    global max_result
    global min_result
    if depth == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    for i, op in enumerate(operstors):
        if not visited[i]:
            visited[i] = True
            prev_result = result
            if op == "+":
                result += numbers[depth]
            elif op == "-":
                result -= numbers[depth]
            elif op == "*":
                result *= numbers[depth]
            else:
                if result > 0:
                    result //= numbers[depth]
                else:
                    result *= -1
                    result //= numbers[depth]
                    result *= -1
                # result = int(result/numbers[depth])
            dfs(result, depth + 1)
            visited[i] = False
            result = prev_result


dfs(numbers[0], 1)
print(max_result)
print(min_result)

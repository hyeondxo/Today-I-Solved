import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(n) for n in input().strip()]

stack = [arr[0]]
x = []
result = []

for i in range(1, n):
    if arr[i] > stack[-1]:
        while stack[-1] < arr[i]:
            x.append(stack.pop())
            if not stack:
                break
            if len(x) == k:
                for j in stack:
                    result.append(j)
                for j in range(i, n):
                    result.append(arr[j])
                for num in result:
                    print(num, end="")
                sys.exit()
        stack.append(arr[i])
    else:
        stack.append(arr[i])

for i in range(0, n-k):
    print(stack[i], end="")

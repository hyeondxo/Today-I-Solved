import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

i = 0
cnt = 0
ans = 0
while i <= m - 3:
    if s[i:i+3] == "IOI":
        cnt += 1
        if n <= cnt:
            ans += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(ans)
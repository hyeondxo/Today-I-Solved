import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
sort_set_arr = sorted(set(arr), key=lambda x: (len(x), x))
sys.stdout.write("\n".join(sort_set_arr))

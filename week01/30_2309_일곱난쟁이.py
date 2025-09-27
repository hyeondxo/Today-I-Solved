import sys
input = sys.stdin.readline

max = 9

talls = [int(input()) for _ in range(max)]

for i in range(max):
    for j in range(max):
        if i == j:
            continue
        exclude_spy = [tall for index, tall in enumerate(
            talls) if index != i and index != j]
        if sum(exclude_spy) == 100:
            exclude_spy.sort()
            sys.stdout.write("\n".join(str(not_spy)
                             for not_spy in exclude_spy))
            sys.exit()

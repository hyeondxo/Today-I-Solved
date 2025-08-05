import heapq
import sys
from typing import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
items = list(map(int, input().split()))
item_count = Counter(items)
using = set()
using_count = 0
remove_count = 0

for i in range(k):
    number = items[i]
    if using_count == n: 
        if number not in using: # 멀티탭이 꽉찼는데 사용중이지 않다면
            # 사용중인 플러그중 가장 늦게 뽑히는 플러그를 뽑음
            latest_index = -1
            remove_plug = None
            for plug in using: # 어떤 플러그를 뽑을지 선택
                found = False
                for j in range(i+1, k):
                    if items[j] == plug: # 뽑을 플러그를 찾았다면 가장 늦게 나오는 플러그로 선택
                        found = True
                        if j > latest_index:
                            latest_index = j
                            remove_plug = plug
                        break
                if not found: # 다시 사용되지 않는다면 뽑는 걸로 선택
                    remove_plug = plug
                    latest_index = float('inf')
                    break
            using.remove(remove_plug)
            using.add(number)
            remove_count += 1

        item_count[number] -= 1
    else: 
        if number not in using: # 멀티탭에 자리가 있는데 사용중이지 않다면 그냥 꼽음
            using.add(number)
            using_count += 1

        item_count[number] -= 1

print(remove_count)

# key : 전기용품 이름, value : 남은 사용 횟수
# 남은 사용 횟수가 적은 것부터 뺌
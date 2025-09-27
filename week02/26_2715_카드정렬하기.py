import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
    sys.exit()
elif n == 2:
    print(cards[0] + cards[1])
    sys.exit()

heapq.heapify(cards)
total = 0
while n > 1:
    cur_sum = heapq.heappop(cards) + heapq.heappop(cards)
    total += cur_sum
    heapq.heappush(cards, cur_sum)
    n -= 1

print(total)

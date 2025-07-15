import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(x) for x in input().split()]
count = 0


def quick_sort(arr, left, right):
    global count
    pl = left + 1
    pr = right
    pivot = arr[left]

    while pl <= pr:
        while arr[pl] < pivot:
            pl += 1
        while arr[pr] > pivot:
            pr -= 1
        if pl <= pr:
            swap_left = arr[pl]
            swap_right = arr[pr]
            arr[pl], arr[pr] = arr[pr], arr[pl]
            count += 1
            if count == k:
                print(swap_left, swap_right)
                sys.exit()
            pl += 1
            pr -= 1

    if left < pr:
        quick_sort(arr, left, pr)
    if right > pl:
        quick_sort(arr, pl, right)


quick_sort(arr, 0, len(arr)-1)
if count < k:
    print(-1)

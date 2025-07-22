def merge_sort(arr, n):
    print(f"{n}번째 호출")
    n += 1
    if len(arr) < 2:
        print(arr)
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], n)
    right = merge_sort(arr[mid:], n)

    return merge(left, right)


def merge(left, right):
    print(f"left = {left}")
    print(f"right = {right}")
    result = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])
    print(f"result = {result}")
    return result


arr = [5, 3, 8, 4, 2, 7, 1, 6]
print(merge_sort(arr, 0))

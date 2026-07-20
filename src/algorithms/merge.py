def merge_sort(arr, start = 0 , end = None):
    if end is None:
        end = len(arr) - 1

    if start  >= end:
        return
    mid = (start + end) // 2
    yield from merge_sort(arr, start, mid)
    yield from merge_sort(arr, mid + 1, end)
    yield from merge(arr, start, mid, end)
def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right =  arr[mid + 1 : end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        yield 'COMPARE', (start + i, mid + 1 + j)
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        yield 'SWAP', (k, arr[k])
        k += 1
    
    while i < len(left):
        arr[k] = left(i)
        yield "SWAP" , (k, arr[k])
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        yield "SWAP" , (k, arr[k])
        j += 1
        k += 1
    yield "DONE", (start, end)
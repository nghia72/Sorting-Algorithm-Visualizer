def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            yield arr, j, j + 1, "compare"
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, j, j + 1, "swap"
    yield arr, -1, -1, "done"


if __name__ == "__main__":
    numbers = [5, 1, 4, 2, 8]
    list(bubble_sort(numbers))
    print("Sorted array:", numbers)


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

array = [70,4, 3, 5,69, 12, 20, 1, 9, 50]

print("Sorted array:", selection_sort(array))
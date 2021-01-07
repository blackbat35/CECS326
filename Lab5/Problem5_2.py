import random
import time


def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    # If left child is greater than root -> swap:
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is greater than root -> swap:
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root
    if largest != i:
        # swap
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


# Build a max heap
def build_max_heap(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)


# Sort an array of given size n by heap_sort
def heap_sort(arr, n):
    build_max_heap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


# Sort an array of given size n by selection_sort
def selection_sort(arr, n):
    for i in range(0, n):
        min_element = i
        for j in range(i+1, n):
            if arr[min_element] > arr[j]:
                min_element = j
        arr[i], arr[min_element] = arr[min_element], arr[i]


# Calculate the average time
telapsed_heap = 0
telapsed_selection = 0
for i in range(0, 100):
    n = 1000
    arr = random.sample(range(-2000, 2000), n)
    arr1 = []

    # Heap sort time
    start_heap = time.time()       # start timer
    heap_sort(arr, n)
    end_heap = time.time()         # end timer
    telapsed_heap = telapsed_heap + (end_heap - start_heap)

    # Selection sort time
    start_selection = time.time()  # start timer
    selection_sort(arr, n)
    end_selection = time.time()    # end timer
    telapsed_selection = telapsed_selection + (end_selection - start_selection)

average_heap = telapsed_heap/100
average_selection = telapsed_selection/100

print("average_heap:     ", average_heap)
print("average_selection:", average_selection)

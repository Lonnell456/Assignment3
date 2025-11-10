import random
import time

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(10000)]
    start = time.time()
    randomized_quicksort(arr, 0, len(arr) - 1)
    end = time.time()
    print(f"Randomized Quicksort completed in {end - start:.5f} seconds.")

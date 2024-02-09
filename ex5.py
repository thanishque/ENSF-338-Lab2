import timeit
import random


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def measure_performance(search_func, vector_size):
    setup = f"from __main__ import {search_func.__name__}; import random; sorted_vector = list(range({vector_size})); target = random.randint(0, {vector_size}-1)"
    total_time = 0
    for _ in range(1000):
        time_taken = timeit.timeit(
            f"{search_func.__name__}(sorted_vector, target)", setup=setup, number=100
        )
        total_time += time_taken
    return total_time / 1000


vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

print("Linear Search:")
for size in vector_sizes:
    avg_time = measure_performance(linear_search, size)
    print(f"Average time for vector size {size}: {avg_time:.6f} seconds")

print("\nBinary Search:")
for size in vector_sizes:
    avg_time = measure_performance(binary_search, size)
    print(f"Average time for vector size {size}: {avg_time:.6f} seconds")

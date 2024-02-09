import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Implementing linear search algorithm
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Implementing binary search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Measure the performance of search algorithms
def measure_performance(search_func, arr, n=1000):
    total_time = 0
    for _ in range(n):
        target = random.choice(arr)
        time_taken = timeit.timeit(lambda: search_func(arr, target), number=100)
        total_time += time_taken
    return total_time / n

# Generate sorted vectors of different sizes
vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
avg_times_linear = []
avg_times_binary = []

for size in vector_sizes:
    sorted_array = np.arange(size)
    avg_time_linear = measure_performance(linear_search, sorted_array)
    avg_time_binary = measure_performance(binary_search, sorted_array)
    avg_times_linear.append(avg_time_linear)
    avg_times_binary.append(avg_time_binary)

# Plotting the performance data and interpolating with appropriate functions
plt.figure(figsize=(10, 6))

# Linear search performance
plt.subplot(1, 2, 1)
plt.plot(vector_sizes, avg_times_linear, 'bo', label='Linear Search')
plt.xlabel('Vector Size')
plt.ylabel('Average Time (s)')
plt.title('Linear Search Performance')

# Interpolating with linear function
def linear_func(x, a, b):
    return a * x + b

params_linear, _ = curve_fit(linear_func, vector_sizes, avg_times_linear)
plt.plot(vector_sizes, linear_func(np.array(vector_sizes), *params_linear), 'r--', label='Linear Fit')

# Binary search performance
plt.subplot(1, 2, 2)
plt.plot(vector_sizes, avg_times_binary, 'go', label='Binary Search')
plt.xlabel('Vector Size')
plt.ylabel('Average Time (s)')
plt.title('Binary Search Performance')

# Interpolating with logarithmic function
def log_func(x, a, b):
    return a * np.log(x) + b

params_log, _ = curve_fit(log_func, vector_sizes, avg_times_binary)
plt.plot(vector_sizes, log_func(np.array(vector_sizes), *params_log), 'r--', label='Logarithmic Fit')

plt.legend()
plt.tight_layout()
plt.show()

# The results for each interpolating function are as expected as linear seach returns a linear graph
# that extends as the items in the array extend according to the complexity o(n.)
# The binary search returns an appropriate logarithmic graph as well which has complexity
# o(log(n)) because it takes a divide and conquer approach it has a less drastic increase in time
# with the increase in number of elements in the array compared to linear search.
# The parameters of the linear function are: 
# a is slope indicating rate of increase in time with complexityand b is the y intercept showing base time
# In logarithmic graph a is the scaling factor influencing rate and b is same as above. 
#  Therefore, the expected result is returned as the experimental time complexity matches theoretical. 

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + \
            int(((float(high - low) /
                (arr[high] - arr[low])) * (x - arr[low])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# 2.1 Interpolation search is advantageous over binary search when data is unevenly distributed, as it estimates the target position based on its value.
#     This leads to faster convergence in such scenarios, potentially resulting in a better best-case time complexity of O(log log n) compared to binary
#     search's O(log n).

# 2.2 Interpolation search assumes a roughly uniform distribution of data. If the actual distribution is different, especially if it's skewed, the estimates
#     used by interpolation search may become inaccurate, leading to suboptimal performance. In such cases, binary search may be more reliable.

# 2.3 To adapt interpolation search to a different distribution, you would need to modify the calculation of `pos` within the while loop. The current formula
#     assumes a linear relationship based on a uniform distribution, so adjusting it to reflect the characteristics of the specific distribution is necessary
#     for accurate estimates.
#     pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

# 2.4 Linear search is the only option when data is unsorted. If sorting is impractical or too costly, and the data is not sorted, linear search is a
#     straightforward and reliable choice.

# 2.5 Linear search may outperform binary and interpolation search when the dataset is small or the target element is near the beginning of the array.
#     In these cases, linear search's simplicity can be more efficient than the log(n) complexity of the other methods.

# 2.6 To improve binary and interpolation search when the target is near the beginning, incorporate an early exit condition in binary search, allowing for
#     quicker termination when the target is found early. Similarly, in interpolation search, check if the estimated position is the target before continuing
#     with additional comparisons, minimizing unnecessary iterations and enhancing performance.

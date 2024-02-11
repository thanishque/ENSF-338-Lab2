def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

# 1.1 This code defines a recursive function `func` to calculate the nth Fibonacci number. If n is 0 or 1, it returns n; otherwise, it recursively adds the results of `func(n-1)` and `func(n-2)`

# 1.2 No, it's not a divide-and-conquer algorithm

# 1.3 The time complexity is exponential: O(2^n)

# 1.4


def fibonacci_memo(n, memo={}):
    if n == 0 or n == 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    return memo[n]


# Example usage:
result = fibonacci_memo(5)
print(result)

# 1.5 The time complexity of the optimized algorithm is O(n)

import cProfile

def sub_function(n):
    # sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

# Use cProfile to profile the execution time of the program
cProfile.run('test_function()', sort='time')
cProfile.run('third_function()', sort='time')

"""
Answers to Questions:

1. What is a profiler, and what does it do?
A profiler, like cProfile or profile in Python, analyzes program performance by tracking 
the frequency and duration of code execution. It provides detailed insights into function, 
method, and code block execution times, aiding developers in identifying performance bottlenecks and areas 
for enhancement. Profilers collect data on call frequencies, individual function times, and 
cumulative execution times, facilitating targeted optimization efforts within the codebase.

2. How does profiling differ from benchmarking?
Benchmarking compares a program's overall performance against criteria or other implementations, offering 
a broad view of efficiency. It's useful for evaluating algorithms, libraries, or hardware configurations. 
Unlike profiling, which targets specific code improvements, benchmarking focuses on general performance assessment.

3. Use a profiler to measure execution time of the program (skip function definitions)
The provided code uses cProfile to measure and profile the execution time of the test_function() and third_function() separately.
By running each function through cProfile.run() with the sort='time' parameter, the execution time of each function is profiled and sorted based on time.

4. Discuss a sample output. Where does execution time go?
Sample Output:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
200000000/1    5.967    0.000    5.967    5.967 ex3.py:4(sub_function)
        1    0.156    0.156    6.123    6.123 ex3.py:11(test_function)
        1    0.001    0.001    6.123    6.123 ex3.py:16(third_function)
    
"""

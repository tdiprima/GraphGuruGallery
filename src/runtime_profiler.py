"""
Demonstrates using VizTracer to profile a sample Python script and view 
the results.
To run: viztracer runtime_profiler.py --output_file result.json
Then: vizviewer result.json
"""

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


result = slow_function()
print(result)

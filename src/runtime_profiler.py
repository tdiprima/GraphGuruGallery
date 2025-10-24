# demonstrates using VizTracer to profile a sample Python script and view the results.
# Note: VizTracer is command-line; this provides a sample script to trace.

# sample_script.py content (save as separate file)
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

result = slow_function()
print(result)

# To run: viztracer runtime_profiler.py --output_file result.json
# Then: vizviewer result.json
# The above commands generate an interactive HTML flame graph of runtime behavior.

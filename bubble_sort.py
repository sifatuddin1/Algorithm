#bubble sort 
import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

input_sizes = [100, 500, 1000, 2000]
times = []

for size in input_sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    bubble_sort(arr.copy())
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(input_sizes, times, marker='o', label="Bubble Sort")
plt.xlabel("Input Size")
plt.ylabel("Time Taken (seconds)")
plt.title("Benchmarking Bubble Sort")
plt.grid()
plt.legend()
plt.show()
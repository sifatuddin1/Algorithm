#selection sort 

import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

input_sizes = [100, 1000, 5000, 10000]
times = []

for size in input_sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    selection_sort(arr.copy())
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(input_sizes, times, marker='o')
plt.xlabel("Input Size")
plt.ylabel("Time Taken (seconds)")
plt.title("Time vs Input Size for Selection Sort")
plt.grid()
plt.show()
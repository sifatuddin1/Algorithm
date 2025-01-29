#insertion sort implementation and benchmarking
import random
import time
import matplotlib.pyplot as plt



def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr




def benchmark_insertion_sort(sizes):
    times = []
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]  
        start = time.time()  
        insertion_sort(data)  
        end = time.time() 
        times.append(end - start)  
    return times


sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]


insertion_times = benchmark_insertion_sort(sizes)


plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o', color='b')
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.title("Benchmarking Insertion Sort Algorithm")
plt.grid(True)
plt.legend()
plt.show()


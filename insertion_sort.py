import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    a = list(arr)
    comparisons = 0
    shifts = 0
    n = len(a)
    
    for i in range(1, n):
        key = a[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
                
        a[j + 1] = key
        
    return comparisons, shifts

def run_experiments():
    ns = [100, 500, 1000, 2000, 3000, 4000, 5000]
    
    sorted_times = []
    reverse_times = []
    random_times = []
    
    for n in ns:
        arr_sorted = list(range(n))
        start = time.time()
        insertion_sort(arr_sorted)
        end = time.time()
        sorted_times.append((end - start) * 1000)
        
        arr_reverse = list(range(n, 0, -1))
        start = time.time()
        insertion_sort(arr_reverse)
        end = time.time()
        reverse_times.append((end - start) * 1000)
        
        arr_random = [random.randint(0, 10000) for _ in range(n)]
        start = time.time()
        insertion_sort(arr_random)
        end = time.time()
        random_times.append((end - start) * 1000)

    plt.figure(figsize=(10, 6))
    plt.plot(ns, sorted_times, label='Sorted (Best Case)', marker='o')
    plt.plot(ns, reverse_times, label='Reverse-Sorted (Worst Case)', marker='o')
    plt.plot(ns, random_times, label='Random (Average Case)', marker='o')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Running Time (ms)')
    plt.title('Empirical Analysis of Insertion Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    run_experiments()
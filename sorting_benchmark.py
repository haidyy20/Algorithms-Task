import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def benchmark():
    sizes = [100, 500, 1000, 2000, 5000]
    
    types = {
        "Sorted": lambda n: list(range(n)),
        "Reversed": lambda n: list(range(n, 0, -1)),
        "Random": lambda n: [random.randint(1, 10000) for _ in range(n)]
    }
    
    for t_name, t_func in types.items():
        print(f"\n--- {t_name} Data ---")
        print(f"{'n':<8} | {'Insertion (s)':<15} | {'Merge (s)':<15} | {'Quick (s)':<15} | {'Python Sort (s)':<15}")
        print("-" * 75)
        
        for n in sizes:
            data = t_func(n)
            
            t1 = time.perf_counter()
            if n <= 2000:
                insertion_sort(data)
            t_ins = time.perf_counter() - t1 if n <= 2000 else float('inf')
            
            t1 = time.perf_counter()
            merge_sort(data)
            t_merge = time.perf_counter() - t1
            
            t1 = time.perf_counter()
            try:
                quick_sort(data)
            except RecursionError:
                pass
            t_quick = time.perf_counter() - t1
            
            t1 = time.perf_counter()
            sorted(data)
            t_py = time.perf_counter() - t1
            
            ins_str = f"{t_ins:.6f}" if n <= 2000 else "SKIPPED"
            print(f"{n:<8} | {ins_str:<15} | {t_merge:<15.6f} | {t_quick:<15.6f} | {t_py:<15.6f}")

if __name__ == "__main__":
    benchmark()
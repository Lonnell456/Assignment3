import random
import time
from hash_table_chaining import HashTable
from randomized_quicksort import randomized_quicksort

def benchmark():
    sizes = [1000, 5000, 10000]
    results = []

    for n in sizes:
        arr = [random.randint(1, 100000) for _ in range(n)]
        start = time.time()
        randomized_quicksort(arr, 0, len(arr) - 1)
        sort_time = time.time() - start

        ht = HashTable()
        start = time.time()
        for i in range(n):
            ht.insert(f"key{i}", i)
        for i in range(n):
            ht.get(f"key{i}")
        hash_time = time.time() - start

        results.append((n, sort_time, hash_time))
        print(f"n={n}: Quicksort={sort_time:.5f}s, HashTable={hash_time:.5f}s")

    with open("DAC_Benchmarks.csv", "w") as f:
        f.write("Input Size,Quicksort Time (s),HashTable Time (s)\n")
        for r in results:
            f.write(f"{r[0]},{r[1]:.5f},{r[2]:.5f}\n")

if __name__ == "__main__":
    benchmark()

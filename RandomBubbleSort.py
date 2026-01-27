import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def generate_dataset(size=10_000):
    # Generate random integers
    return [random.randint(1, 100_000) for _ in range(size)]

def main():
    print("=" * 50)
    print("BUBBLE SORT PERFORMANCE ANALYSIS")
    print("=" * 50)

    data = generate_dataset()
    print(f"Dataset size: {len(data)} elements")

    start_time = time.perf_counter()
    sorted_data = bubble_sort(data)
    end_time = time.perf_counter()

    print("\nSorted Array Preview:")
    print("First 20 elements:")
    print(sorted_data[:20])

    print("\nLast 20 elements:")
    print(sorted_data[-20:])

    print("\nExecution Time:")
    print(f"{end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()

import time
import sys
from typing import List, Tuple

def bubble_sort(arr: List[int], order: str = "ascending") -> Tuple[List[int], float]:
    """
    Sorts an array using bubble sort in ascending or descending order.

    Args:
        arr: list of integers
        order: "ascending" (default) or "descending"

    Returns:
        (sorted_list, time_taken_seconds)
    """
    start = time.perf_counter()
    n = len(arr)

    ascending = order.lower().startswith('a')

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    end = time.perf_counter()
    return arr, end - start


def print_result(original, sorted_arr, time_taken, order):
    print("Original:", original)
    print(f"Sorted ({order.title()}):", sorted_arr)
    print("Array Size:", len(sorted_arr))
    print(f"Time: {time_taken:.6f} seconds ({time_taken*1000:.3f} ms)\n")


if __name__ == "__main__":
    # If the user passes numbers and order via command line:
    # Usage examples:
    #   python bubblesort.py "64,34,25,12,22,11,90" ascending
    #   python bubblesort.py "5 1 4 2 8" descending
    # or run with no args to demo some examples below.

    if len(sys.argv) >= 2:
        raw = sys.argv[1]
        # Accept comma-separated or space-separated inputs
        if ',' in raw:
            arr = [int(x.strip()) for x in raw.split(',') if x.strip() != ""]
        else:
            arr = [int(x.strip()) for x in raw.split() if x.strip() != ""]
        order = sys.argv[2] if len(sys.argv) >= 3 else "ascending"
        sorted_arr, t = bubble_sort(arr.copy(), order)
        print_result(arr, sorted_arr, t, order)
    else:
        # Demo arrays
        examples = [
            ([64, 34, 25, 12, 22, 11, 90], "ascending"),
            ([5, 1, 4, 2, 8], "descending"),
            ([1, 2, 3, 4, 5], "ascending"),
            ([5, 4, 3, 2, 1], "descending"),
        ]
        for arr, order in examples:
            sorted_arr, t = bubble_sort(arr.copy(), order)
            print_result(arr, sorted_arr, t, order)

        # Optional: load dataset.txt (if you want to sort values from your uploaded dataset)
        try:
            with open("dataset.txt", "r") as f:
                nums = [int(line.strip()) for line in f if line.strip() != ""]
            if nums:
                print("Sorting dataset.txt (first 20 shown)...")
                sorted_nums, t = bubble_sort(nums.copy(), "ascending")
                print("First 20 sorted values:", sorted_nums[:20])
                print(f"Dataset size: {len(nums)}. Time: {t:.6f} seconds ({t*1000:.3f} ms)\n")
        except FileNotFoundError:
            pass

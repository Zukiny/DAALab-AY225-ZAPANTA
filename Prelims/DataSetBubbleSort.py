import csv
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ================= Sorting algorithms =================
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ================= Data loading =================
def try_convert(item):
    """Try to convert item to float, otherwise keep as string."""
    try:
        return float(item)
    except ValueError:
        return str(item)

def load_file():
    Tk().withdraw()  # Hide the root Tk window
    filename = askopenfilename(title="Select a data file", 
                               filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
    if not filename:
        print("No file selected.")
        return []

    data = []
    try:
        if filename.endswith('.txt'):
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data.append(try_convert(line))
        elif filename.endswith('.csv'):
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    for item in row:
                        item = item.strip()
                        if item:
                            data.append(try_convert(item))
        print(f"Loaded {len(data)} items from {filename}")
    except Exception as e:
        print(f"Error loading file: {e}")
    return data

# ================= Handle mixed datasets =================
def sort_mixed_data(data, algorithm_func):
    """Sort numbers and strings together: numbers first, strings after."""
    numbers = [x for x in data if isinstance(x, (int, float))]
    strings = [x for x in data if isinstance(x, str)]

    sorted_numbers = algorithm_func(numbers)
    sorted_strings = algorithm_func(strings)

    return sorted_numbers + sorted_strings

# ================= Main Program =================
def main():
    print("=== Data Sorting System ===")
    data = load_file()
    if not data:
        return

    print("\nChoose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    choice = input("Enter choice (1-3): ")

    if choice == '1':
        algorithm = bubble_sort
        algo_name = "Bubble Sort"
    elif choice == '2':
        algorithm = insertion_sort
        algo_name = "Insertion Sort"
    elif choice == '3':
        algorithm = merge_sort
        algo_name = "Merge Sort"
    else:
        print("Invalid choice.")
        return

    # Measure runtime
    start_time = time.time()
    sorted_data = sort_mixed_data(data, algorithm)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nSorted data using {algo_name}:")
    print(sorted_data)
    print(f"\nSorting runtime: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    main()

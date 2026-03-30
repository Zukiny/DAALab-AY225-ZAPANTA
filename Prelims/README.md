# Sorting Algorithms Lab

This repository contains two Python programs that implement classic sorting algorithms and analyze their performance. These programs are designed for educational purposes to demonstrate the difference between **quadratic-time sorts** (Bubble Sort, Insertion Sort) and **log-linear-time sorts** (Merge Sort), as well as how data input methods affect performance.

---

## Programs Included

### 1. `RandomBubbleSort.py`

**Purpose:**  
This program generates a **random dataset** of integers of a user-specified size and sorts it using a selected algorithm.

**Supported Algorithms:**

- **Bubble Sort** (optimized) – O(n²) exchange sort  
- **Insertion Sort** – O(n²) comparison sort  
- **Merge Sort** – O(n log n) divide-and-conquer sort  

**How It Works:**

1. Prompts the user to enter the dataset size (e.g., 10,000).  
2. Generates a list of random integers of that size.  
3. Prompts the user to choose a sorting algorithm.  
4. Runs the selected algorithm and measures **execution time**.  
5. Verifies that the list is sorted correctly.  
6. Displays a preview of the first and last 20 elements.  
7. Shows execution time and complexity notes.

**Bubble Sort Type Used:**  
- **Optimized Bubble Sort:** Includes a check to stop the algorithm early if no swaps occur during a pass, reducing unnecessary iterations.

---

### 2. `DataSetBubbleSort.py`

**Purpose:**  
This program allows the user to sort a dataset **from a CSV file stored in their Documents folder**, automatically detecting the dataset size and using only the integers in the file.

**Supported Algorithms:**

- **Bubble Sort** (optimized) – O(n²) exchange sort  
- **Insertion Sort** – O(n²) comparison sort  
- **Merge Sort** – O(n log n) divide-and-conquer sort  

**How It Works:**

1. Prompts the user to select the data source:
   - **Documents CSV**  
2. If **Documents** is selected:
   - Opens the file picker in the user's **Documents folder**.  
   - Reads integers from the **first column** of the CSV file.  
   - Automatically detects dataset size from the file.  
3. Prompts the user to choose a sorting algorithm.  
4. Runs the selected algorithm and measures **execution time**.  
5. Verifies that the list is sorted correctly.  
6. Displays a preview of the first and last 20 elements.  
7. Shows execution time and complexity notes.

**Bubble Sort Type Used:**  
- **Optimized Bubble Sort:** Stops early if no swaps occur in a pass.

**Special Features:**

- Uses Tkinter to open a **file picker** directly in the Documents folder.  
- Works reliably on Windows, Mac, and Linux without freezing the console.  

---

## Sorting Algorithms Overview

| Algorithm       | Time Complexity | Type                         |
|-----------------|----------------|------------------------------|
| Bubble Sort      | O(n²)          | Quadratic, exchange sort      |
| Insertion Sort   | O(n²)          | Quadratic, comparison sort   |
| Merge Sort       | O(n log n)     | Divide-and-conquer           |

**Notes:**

- Bubble Sort and Insertion Sort are slower for large datasets due to their quadratic nature.  
- Merge Sort scales efficiently for larger datasets because of its log-linear time complexity.

---

## How to Run

### Random Dataset Program:

```bash
python [FileName].py

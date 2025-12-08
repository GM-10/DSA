# Sorting Algorithms – Selection, Bubble, Insertion, Merge & Quick Sort

This document explains major comparison-based sorting algorithms: **Selection Sort**, **Bubble Sort**, **Insertion Sort**, **Merge Sort**, and **Quick Sort** — including both iterative and recursive versions where applicable.

---

## 📌 1. Selection Sort

### 📍 Definition  
Selection Sort sorts an array by **repeatedly finding the minimum element** from the unsorted region and placing it at the beginning.

### 🔹 Key Points
- Works by dividing array into **sorted** and **unsorted** parts
- Select the **minimum** element in each pass
- Swap with the leftmost unsorted element

### 📊 Complexity
| Case | Time |
|------|------|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) |

### 📌 Stability  
❌ Not Stable  

---

## 📌 2. Bubble Sort

### 📍 Definition  
Repeatedly compares adjacent elements and swaps them if in wrong order. Large values **bubble up** to the end.

### 🔹 Optimized Bubble Sort  
Stops early if no swap happens → **Best case O(n)**.

### 📊 Complexity
| Case | Time |
|------|------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) |

### 📌 Stability  
✔️ Stable  

---

## 📌 3. Insertion Sort

### 📍 Definition  
Sorts array by building sorted list **one element at a time**, inserting each element into correct place.

### 📊 Complexity
| Case | Time |
|------|------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) |

### 📌 Stability  
✔️ Stable  

---

## 📌 4. Recursive Bubble Sort

### 📍 Definition  
Same concept as Bubble Sort, but implemented using **recursion** instead of loops.

### 🔹 Key Points  
- In each recursive call, the largest element settles at the end
- Then sort remaining (n-1) elements recursively

### 📊 Complexity  
| Case | Time |
|------|------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(n) (due to recursion stack) |

### 📌 Stability  
✔️ Stable  

---

## 📌 5. Merge Sort (Iterative)

### 📍 Definition  
Divide-and-Conquer sorting method that repeatedly **splits array** into smaller parts and merges them in sorted order.

### 🔹 Key Points  
- Bottom-up merging (iterative)
- Always divides into halves and merges sorted subarrays
- Requires **extra space**

### 📊 Complexity  
| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |
| Space | O(n) |

### 📌 Stability  
✔️ Stable  

---

## 📌 6. Recursive Merge Sort

### 📍 Definition  
Classic divide-and-conquer sorting:  
➡️ Split → Sort (recursively) → Merge

### 🔹 Key Points  
- Recursively breaks array into 2 halves until single element remains
- Then merges them in sorted order

### 📊 Complexity  
Same as iterative merge sort.  
| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |
| Space | O(n) |

### 📌 Stability  
✔️ Stable  

---

## 📌 7. Quick Sort

### 📍 Definition  
Divide-and-Conquer algorithm that partitions the array using a **pivot**, placing elements smaller than pivot to left and greater to right.

### 🔹 Key Points  
- Very fast in practice  
- Performance depends on pivot choice  
- In-place method (low memory usage)

### 📊 Complexity  
| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n²) |
| Space | O(log n) (recursion stack) |

### 📌 Stability  
❌ Not Stable (depends on implementation)

---

## 🔍 Quick Comparison Table

| Algorithm | Best Case | Avg Case | Worst Case | Space | Stable |
|----------|-----------|----------|------------|-------|--------|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✔️ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✔️ |
| Recursive Bubble | O(n) | O(n²) | O(n²) | O(n) | ✔️ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✔️ |
| Recursive Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✔️ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |

---

## 🧠 Summary & Usage

| Algorithm | Best Used When |
|----------|----------------|
| Selection Sort | Swaps should be minimized |
| Bubble Sort | Nearly sorted and simple to implement |
| Insertion Sort | Small or nearly sorted datasets |
| Merge Sort | Large datasets, stable sorting needed |
| Quick Sort | Best practical performance, average very fast |

---


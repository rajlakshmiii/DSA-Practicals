# Selection Sort
def selection_sort(salaries):
    arr = salaries.copy()
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Bubble Sort
def bubble_sort(salaries):
    arr = salaries.copy()
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop early if no swapping occurs
        if not swapped:
            break

    return arr


# Employee Salaries
salaries = [
    45000.50,
    72000.75,
    38000.25,
    95000.00,
    61000.50,
    55000.75,
    88000.25,
    42000.00,
    105000.50,
    67000.25
]

# Selection Sort
selection_result = selection_sort(salaries)

print("Original Salaries:")
print(salaries)

print("\nSalaries after Selection Sort:")
print(selection_result)

print("\nTop Five Highest Salaries using Selection Sort:")
for salary in selection_result[-5:][::-1]:
    print(salary)

# Bubble Sort
bubble_result = bubble_sort(salaries)

print("\nSalaries after Bubble Sort:")
print(bubble_result)

print("\nTop Five Highest Salaries using Bubble Sort:")
for salary in bubble_result[-5:][::-1]:
    print(salary)
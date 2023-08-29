#insertionsort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared

        # Move elements of arr[0...i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in its correct position

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)

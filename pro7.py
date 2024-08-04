def insertion_sort(elements):
    # Iterate over each element starting from the second element
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        
        # Move elements of elements[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]
            j -= 1
        
        # Place the key at the correct position
        elements[j + 1] = key

    return elements

# List of elements to be sorted
elements = [1, 4, 2, 8, 23]

# Sorting the list
sorted_elements = insertion_sort(elements)

# Print the sorted list
print("Sorted elements:", sorted_elements)

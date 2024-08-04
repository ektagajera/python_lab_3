def selection_sort(elements):
    n = len(elements)
    
    for i in range(n):
        # Assume the current position holds the minimum value
        min_index = i
        
        # Find the index of the smallest element in the remaining unsorted portion
        for j in range(i+1, n):
            if elements[j] < elements[min_index]:
                min_index = j
        
        # Swap the found smallest element with the element at the current position
        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]
    
    return elements

# List of elements to be sorted
elements = [22, 13, 4, 8, 17, 26, 53, 4]

# Sorting the list
sorted_elements = selection_sort(elements)

# Print the sorted list
print("Sorted elements:", sorted_elements)

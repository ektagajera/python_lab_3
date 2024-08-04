def sequential_search(elements, target):
    """
    Perform a sequential search for the target value in the list of elements.

    Args:
    elements (list): The list of elements to search through.
    target (int): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index in range(len(elements)):
        if elements[index] == target:
            return index
    return -1

# List of elements to search through
elements = [1, 3, 5, 8, 10, 23, 35]

# Target value to search for
target = 10

# Perform the sequential search
index = sequential_search(elements, target)

# Output the result
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")

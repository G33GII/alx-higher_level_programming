def find_peak(list_of_integers):
    # Define the bounds of the search space
    left = 0
    right = len(list_of_integers) - 1

    # Perform binary search
    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # Return the peak element
    return list_of_integers[left]


# Test the function
print(find_peak([1, 3, 20, 4, 1, 0]))  # Example test case

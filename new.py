def find_largest_number(numbers):
    # Check if the list is empty
    if not numbers:
        return None  # Return None or an appropriate value for an empty list

    # Initialize the largest number as the first element of the list
    largest_number = numbers[0]

    # Loop through the list starting from the second element
    for number in numbers[1:]:
        # Compare the current number with the largest number found so far
        if number > largest_number:
            # Update the largest number if the current number is greater
            largest_number = number

    # Return the largest number found
    return largest_number

# Example usage:
numbers = [3, 5, 7, 2, 8, 6]
print("The largest number is:", find_largest_number(numbers))


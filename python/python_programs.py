# Find the second-highest number in a list.
def second_highest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Not enough unique numbers to find the second highest
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1]  # Return the second highest number

# Find the second-highest number in a list without sorting.
def second_highest_without_sorting(numbers):
    first = second = float('-inf')  # Initialize to negative infinity
    for number in numbers:
        if number > first: # here we are checking if the number is greater than the first highest number
            second = first # Update the second highest number
            first = number # Update the highest number
        elif first > number > second: # here we are checking if the number is greater than the second highest number and less than the first highest number
            second = number # Update the second highest number
    return second if second != float('-inf') else None  # Return None if no second highest exists
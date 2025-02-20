def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers)

# Example usage with error handling
averages = []
data = [[1, 2, 3], [], [4, 5], [6]]
for lst in data:
    avg = calculate_average(lst)
    averages.append(avg)
print(averages) # Output: [2.0, 0, 4.5, 6.0]
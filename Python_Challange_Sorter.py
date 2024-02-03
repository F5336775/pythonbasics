def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        # List of float point numbers for accuracy and precision
        numbers = [float(line.strip()) for line in file]
    return numbers


def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")
    print(f"Sorted numbers saved to {filename}")


# Timsort default sorting algorithm
def sort_numbers(numbers):
    # Using built-in sorted function for simplicity
    return sorted(numbers)


# Bubble sort algorithm
# Time complexity of o(n^2)
def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

# Merge sort
# Time complexity of o(nlogn)
def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in both halves
        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

    return numbers


def main():
    input_filename = "Unsorted_Values.txt"
    output_filename = "Values_Sorted.txt"

    # Read numbers from the unsorted file
    numbers = read_numbers_from_file(input_filename)

    # Sort the numbers
    sorted_numbers = merge_sort(numbers)

    # Write the sorted numbers to the output file
    write_numbers_to_file(output_filename, sorted_numbers)


if __name__ == "__main__":
    main()

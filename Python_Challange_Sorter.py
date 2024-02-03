def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        # Array of float point numbers for accuracy and precision
        numbers = [float(line.strip()) for line in file]
    return numbers


def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")
    print(f"Sorted numbers saved to {filename}")


def sort_numbers(numbers):
    # Using built-in sorted function for simplicity
    # Timsort default sorting algorithm
    return sorted(numbers)


def main():
    input_filename = "Unsorted_Values.txt"
    output_filename = "Values_Sorted.txt"

    # Read numbers from the unsorted file
    numbers = read_numbers_from_file(input_filename)

    # Sort the numbers
    sorted_numbers = sort_numbers(numbers)

    # Write the sorted numbers to the output file
    write_numbers_to_file(output_filename, sorted_numbers)


if __name__ == "__main__":
    main()

import random


def generate_unsorted_file(filename, num_numbers):
    with open(filename, 'w') as file:
        for _ in range(num_numbers):
            random_number = random.randint(1, 100000)
            file.write(f"{random_number}\n")


generate_unsorted_file("Unsorted_Values.txt", 50000)
print("Unsorted numbers file generated.")

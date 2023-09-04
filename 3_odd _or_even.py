even_count = 0
odd_count = 0
input_str = input("Enter a series of numbers separated by spaces: ")
numbers = input_str.split()
for num in numbers:
    try:
        num = int(num)
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    except ValueError:
        print(f"Skipping invalid input: {num}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

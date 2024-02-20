def generate_even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))

even_numbers_generator = generate_even_numbers(n)

even_numbers_str = ', '.join(map(str, even_numbers_generator))

print("Even numbers between 0 and", n, ":", even_numbers_str)

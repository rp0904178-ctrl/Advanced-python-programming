# Experiment No. 4
# Efficient Fibonacci using Fast Doubling

def fibonacci(n):
    # Base case
    if n == 0:
        return (0, 1)

    # Recursive fast doubling
    a, b = fibonacci(n // 2)

    # F(2k)
    c = a * (2 * b - a)

    # F(2k + 1)
    d = a * a + b * b

    if n % 2 == 0:
        return (c, d)
    else:
        return (d, c + d)


# Main Program
print("===== Efficient Fibonacci Calculator =====")

n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = fibonacci(n)[0]
    print(f"The {n}th Fibonacci number is: {result}")

def recursive_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    fib_series = [0, 1]
    if n <= 1:
        return fib_series[:n + 1]
    else:
        for i in range(2, n):
            fib_series.append(fib_series[i - 1] + fib_series[i - 2])
        return fib_series

# Taking user input for n
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Example usage for recursive Fibonacci:
print("\nRecursive Fibonacci:")
for i in range(n):
    print(recursive_fibonacci(i))

# Example usage for non-recursive Fibonacci:
print("\nNon-Recursive Fibonacci:")
result = non_recursive_fibonacci(n)
print(result)

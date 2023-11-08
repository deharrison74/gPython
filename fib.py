def fibonacci_series(n):
    fib = [0, 1]
    for i in range(2, n):
        next_term = fib[i - 1] + fib[i - 2]
        fib.append(next_term)
    return fib

# Get Input
n = int(input("Enter the value of n: "))

# Call the function
fib = fibonacci_series(n)

print("Fibonacci series up to " + str(n) + " terms: ")
for term in fib:
    print(term, end=" ")

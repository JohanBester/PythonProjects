# Fibonacci series:
# where the sum of two elements defines the next

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b, sum = 0, 1, 0
    fibNums = []

    print("\nThe sum of all the Fibonacci numbers between 0 and",
          n, "listed below, follows...")

    while a < n:
        fibNums.append(a)
        print(a, end=' ')
        sum, a, b = sum+a, b, a+b
    print('... And the sum = ', sum)

    return print(fibNums)


f1000 = fib(1000)
f2000 = fib(2000)
f5000 = fib(5000)

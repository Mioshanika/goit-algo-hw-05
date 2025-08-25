def caching_fibonacci():
    fibonacci_cache = {}
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in fibonacci_cache.keys():
            return fibonacci_cache[n]
        fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibonacci_cache[n]
    return fibonacci

def main():
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

if __name__ == '__main__':
    main()
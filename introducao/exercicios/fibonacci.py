def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib_n_2 = 0
    fib_n_1 = 1
    
    # Calculando os números subsequentes da sequência
    for _ in range(2, n + 1):
        fib = fib_n_1 + fib_n_2
        fib_n_1 = fib
        fib_n_2 = fib_n_1
    
    return fib


print(fibonacci(6))

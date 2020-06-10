def fib2(n: int) -> int:
    """Método que calcula un término de la secuencia fibonacci con casos base. """

    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)

if __name__ == '__main__':
    print(fib2(5))
    print(fib2(10))
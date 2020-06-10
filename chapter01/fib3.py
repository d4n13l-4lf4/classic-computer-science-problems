from chapter01.util import memoization


@memoization
def fib3(n: int) -> int:
    """Método que calcula un término de la secuencia fibonacci utilizando memorización. """
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)


if __name__ == '__main__':
    print(fib3(5))
    print(fib3(10))
    print(fib3(50))
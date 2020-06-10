def fib1(n: int) -> int:
    """Método que calcula un término fibonacci recursivamente sin límite (recursión infinita)!"""
    return fib1(n - 1) + fib1(n - 2)

if __name__ == '__main__':
    print(fib1(5))
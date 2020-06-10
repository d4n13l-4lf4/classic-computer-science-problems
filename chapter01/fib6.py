from typing import Generator

def fib6_gen(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    generator = fib6_gen(50)

    for i in generator:
        print(i)

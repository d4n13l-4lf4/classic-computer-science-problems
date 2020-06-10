from functools import wraps

def memoization(f):
    cache = dict()

    @wraps(f)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

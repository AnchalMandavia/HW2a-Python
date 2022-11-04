from time import time

def timeme(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Total time {(end-start):.4f}s')
        return result
    return wrapper_func
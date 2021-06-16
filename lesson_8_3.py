from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = [f'{i}: {type(i)}' for i in args]
        print('position arguments:', ', '.join(result))
        if kwargs:
            result_dict = [f'key-{k}, value-{v}: {type(v)}' for k, v in kwargs.items()]
            print('key arguments:', ', '.join(result_dict))
        print(f'call {func.__name__}(result {func(*args, **kwargs)}: {type(func(*args, **kwargs))})')

        return func(*args, **kwargs)

    return wrapper


def calc_cube(x):
    return x ** 3


a = type_logger(calc_cube)
print(a(5))

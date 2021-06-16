from functools import wraps


def val_checker(input_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if input_func(*args):
                return func(*args)
            else:
                msg = f'wrong value {",".join(map(str, args))}'
                raise ValueError(msg)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))

from datetime import datetime
class Validator:
    def __init__(self, lower, upper):
        self._lower = lower
        self._upper = upper

    def __call__(self, arg):
        def wrapper(a):
            rez = arg(a)
            if not self._lower < rez < self._upper:
                raise ValueError('Validator failed')
            return f'{datetime.now()}: {rez} '
        return wrapper


# @Validator(0, 10)
def square(a):
    return a**2

validate_square = Validator(0, 10) (square)
print(validate_square(2))

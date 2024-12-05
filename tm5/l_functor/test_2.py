from datetime import datetime

class Validator:
    def __init__(self, function):
        self.function = function
    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        if not 0 < result < 100:
            raise ValueError('result must be between 0 and 100')
        return f'{datetime.now()} : {result}'

@Validator
def square(a):
    return a**2

print(square(8))
print(square(12))
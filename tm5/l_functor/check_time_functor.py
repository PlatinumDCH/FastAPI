import time
from functools import wraps  #сохранение ссылки на оригинальную функцию

class RegisterTime:
    def __init__(self, label='Execution Time'):
        self.label = label

    def __call__(self, func):
        @wraps(func) #сохраняем метаданные на функцию
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            executed_time = time.time() - start_time
            print(f'{self.label}: {executed_time:.4f} seconds')
            return result
        return wrapper

def exemple_function(timer:int):
    time.sleep(timer)
    return 'exemple result'

# decorated_function= RegisterTime()(exemple_function)
# result_function = decorated_function(1)
# print(result_function)

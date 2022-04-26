import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Time taken by function: ", func.__name__, " is: ", str((end_time - start_time)*1000), "ms")
        return result
    return wrapper

  

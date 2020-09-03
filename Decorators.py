import functools
import time

# -Print the runtime of the decorated function

def timer(func):

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):

        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)

        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3

        print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
        return value

    return wrapper_timer

@timer
def calculating_something(*args):

   return sum(x*x for x in args)

print(calculating_something(12, 15, 20, 29, 88, 235))
print(calculating_something(2, 3))





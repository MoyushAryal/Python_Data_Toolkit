import time


def log_time(func):

    def wrapping_function(*args):
        timer_start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        time_taken = end-timer_start

        print(f"{func.__name__} took {time_taken} seconds")

        return result
    return wrapping_function
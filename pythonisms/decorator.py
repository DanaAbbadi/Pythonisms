import functools
import time
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def factors1(n):
    results = [ ]
    for k in range(1,n+1):
        if n % k == 0: results.append(k)
    return results

@slow_down
def factors2(n):
    for k in range(1,n+1):
        if n % k == 0: 
            yield k
print(factors1(100))

for factor in factors2(100):
    print(factor)
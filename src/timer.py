import time
from decimal import Decimal

def dectimer(func) -> Decimal:
    """This is a decorator which is used to calculate the time taken by a function.
    It returns time in seconds represented by Decimal datatype.

    Args:
        func (function): The function you want to calculate the time for.

    Returns:
        Decimal: The time taken by the function in seconds.
    """    
    def wrapper():
        start = Decimal(time.perf_counter())
        func()
        end = Decimal(time.perf_counter())
        return end - start
    return wrapper

def decptimer(func) -> Decimal:
    """This is a decorator which is used to calculate the time taken by a function.
    It prints the time in seconds represented by Decimal datatype.

    Args:
        func (function): The function you want to calculate the time for.
    """   
    def wrapper():
        start = Decimal(time.perf_counter())
        func()
        end = Decimal(time.perf_counter())
        time_taken = str(end - start).strip("Decimal()")
        print(f"Time taken : {time_taken}s")
    return wrapper

@dectimer
def test():
    time.sleep(1)

@decptimer
def test2():
    time.sleep(1)

if __name__ == "__main__":
    """To run the demo functions of the module.
    """    
    print(test())
    test2()
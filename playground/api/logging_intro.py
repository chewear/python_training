
from util.logger import Logger 


# test_logs()
# logger1 = Logger().get_logger()
# logger2 = Logger().get_logger()
# logger3 = Logger().get_logger()

# logger1.info("test1")
# logger2.info("test2")
# logger3.info("test3")
# print("Logging Completed")
#===================
# def my_decorator(param):  
#     def decorator(func):  
#         def wrapper(*args, **kwargs):
#             print(f"Begin: {param}")         
#             result = func(*args, **kwargs)  
#             print("End additional behavior")
#             return result
#         return wrapper
#     return decorator
#===================

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"begin {func.__name__}")
        result = func(*args, **kwargs)
        print(f"end {func.__name__}")
        return result
    return wrapper


@my_decorator
def add(*args):
    sum = 0
    for a in args:
        sum += a
    print(sum)

@my_decorator
def test(**kwargs):
    print(kwargs)

@my_decorator
def all(*args, **kwargs):
    print(args)
    print(kwargs)

add(1,2,3,4)
test(v1=1, v2=2)
# all(1,2,3,4, v1=1, v2=2)


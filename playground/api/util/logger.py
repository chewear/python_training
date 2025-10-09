import logging
from logging import Logger as PythonLogger
from functools import wraps

class Logger:
    def __init__(self):
        self.__logger:PythonLogger = logging.getLogger("my_app")
        formatter = '%(asctime)s - %(name)s - %(levelname)s \t %(filename)s \t %(funcName)s \t %(lineno)d  %(message)s'
        logging.basicConfig(filename='myapp.log', level=logging.DEBUG, format=formatter)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def get_logger(self) -> PythonLogger:
        return self.__logger

def enable_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        Logger().get_logger().info(f"Starting function: \t {func.__name__}")
        if args or kwargs:
            Logger().get_logger().info(f"Params: \t [{args}] - [{kwargs}]")
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            Logger().get_logger().error(ex, exc_info=True)
            raise Exception(ex)
        
        Logger().get_logger().info(f"Ending function \t {func.__name__}")
        return result
    return wrapper

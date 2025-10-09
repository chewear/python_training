import logging
from logging import Logger

logger:Logger = logging.getLogger("my_app")
formatter = '%(asctime)s - %(name)s - %(levelname)s \t %(filename)s \t %(funcName)s \t %(lineno)d  %(message)s'
logging.basicConfig(filename='myapp.log', level=logging.DEBUG, format=formatter)
def test_logs():
    logger.info("This is an info")
    logger.warning("This is a warning")
    logger.debug("This is a debug")
    logger.error("This is an error")

test_logs()
print("Logging Completed")


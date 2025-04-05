from DVP.logger import logging
from DVP.exception import USvisaException
import sys

logging.info("Welcome to custom log!")


try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)
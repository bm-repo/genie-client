from functools import wraps
from time import time

import loggers.app_logger as app_logger

logger = AppLoggerFactory().logger

def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        
        ts = time()
        result = f(*args, **kw)
        te = time()

        logger.info(f'Function {f.__name__} took {te-ts:2.4f} seconds')

        return result
    return wrap

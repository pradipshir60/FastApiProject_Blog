import logging
import logging.handlers
import os

def get(): 
    handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "logs\\app.log"))
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)
    return logging
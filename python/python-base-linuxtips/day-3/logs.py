#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE Code

# TODO: Use function
# TODO: Use Lib (libguru)

# Setting the log level to a env variable
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Setting our instance to start logging.
log = logging.Logger("logs.py", log_level)

fh = handlers.RotatingFileHandler(
    "myprogram.log", 
    maxBytes=100, 
    backupCount=10
)
fh.setLevel(log_level)
# Formatting logs
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    " line:%(lineno)d f:%(filename)s: %(message)s"
)
fh.setFormatter(fmt)
# Logs destination
log.addHandler(fh)

"""
log.debug("DEV ERROR: ")
log.info("ALL USERS ERROR:")
log.warning("WARNING:")
log.error("ERROR:")
log.critical("CRITICAL:")
"""

print("--------")

try: 
    1/0
except ZeroDivisionError as e:
    log.critical("ERROR: %s", str(e))
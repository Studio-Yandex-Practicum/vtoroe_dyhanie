import datetime
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from .settings import settings


logger = logging.getLogger(__name__)

p = Path(settings.logging_dir)
if not os.path.exists(p):
    os.makedirs(p)
logging.basicConfig(
    level=settings.logging_level,
    format=settings.logging_format,
    handlers=[TimedRotatingFileHandler(
        f"{p}/{datetime.date.today()}.log",
        when='D',
        interval=1,
        backupCount=60,),
            logging.StreamHandler(stream=sys.stdout)])

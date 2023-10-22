import datetime
import logging
import logging.config
import os
from pathlib import Path

from .settings import settings


p = Path(settings.logging_dir)
if not os.path.exists(p):
    os.makedirs(p)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'default': {'format': settings.logging_format}},
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'level': settings.logging_level,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': f'{p}/{datetime.date.today()}.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 60,
        },
    },
    'loggers': {
        '': {
            'handlers': ['stdout', 'file'],
            'level': settings.logging_level,
            'propagate': True,
        }
    },
}


logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)

from datetime import datetime
from loguru import logger

def ping():
    logger.info(f'Scheduler is alive!')
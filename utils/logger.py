import logging
import os

LOG_DIR = "logs"
LOG_FILE = "discord-bot.log"

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE), encoding='utf-8')
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

import logging
import logging.handlers
import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# Configuration 

LOG_DIR = Path(os.getenv("LOG_DIR", "logs"))
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE_NAME = os.getenv("LOG_FILE_NAME", "app.log")

MAX_LOG_SIZE = int(os.getenv("LOG_MAX_SIZE", 10 * 1024 * 1024))
BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", 5))

ENV = os.getenv("ENV", "development").lower()


# Logger Factory 

def get_logger(
    name: Optional[str] = None,
) -> logging.Logger:
    """
    Returns a configured logger instance.
    Safe to call multiple times across the app.
    """

    logger_name = name if name else "app"
    logger = logging.getLogger(logger_name)

    # Prevent duplicate handlers if already configured
    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)
    logger.propagate = False

    # Formatters 

    standard_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    detailed_formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | %(levelname)s | %(name)s | "
            "%(filename)s:%(lineno)d | %(funcName)s() | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    formatter = detailed_formatter if ENV == "development" else standard_formatter

    # Console Handler 

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler (Rotating) 

    file_handler = logging.handlers.RotatingFileHandler(
        LOG_DIR / LOG_FILE_NAME,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
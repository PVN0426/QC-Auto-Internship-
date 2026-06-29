import logging
import os


def get_logger():

    os.makedirs(
        "results/logs",
        exist_ok=True
    )

    logger = logging.getLogger()

    logger.setLevel(
        logging.INFO
    )
# INFO
# WARNING
# ERROR
# CRITICAL
    if not logger.handlers:

        file_handler = logging.FileHandler(
            "results/logs/test_execution.log",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

    return logger
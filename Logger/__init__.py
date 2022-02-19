import logging


def get_logger(name: str) -> logging:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        format="[%(levelname)s] - %(asctime)s - %(name)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    return logger

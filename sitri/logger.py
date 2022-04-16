import logging
import typing


def get_default_logger(name: typing.Optional[str] = None) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )

    return logging.getLogger(name or "sitri.default")

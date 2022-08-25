from __future__ import annotations

import logging


def get_default_logger(name: str | None = None) -> logging.Logger:
    """get_default_logger.

    :param name:
    :type name: t.Optional[str]
    :rtype: logging.Logger
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )

    return logging.getLogger(name or "sitri.default")

# Logging

You can pass your logger (structlog, loguru or your own configured
logging.Logger) to sitri for one-style logs.

Examples:

1.  Providers

    > ``` python
    > from sitri.strategy.index_priority import IndexPriorityStrategy
    > from sitri.contrib.system import SystemConfigProvider
    > from sitri.contrib.json import JsonConfigProvider
    >
    > from myapp.logs import get_logger
    >
    > system_conf = SystemConfigProvider(
    >     prefix="project", logger=get_logger(name="sitri.system_conf.1")
    > )
    > json_conf = JsonConfigProvider(logger=get_logger(name="sitri.json_conf.1"))
    > ```

2.  Settings

    > In settings config-class property *local_provider_logger*, you can
    > pass logger for *local_mode* provider (default: json).

# Sitri - powerful settings & configs for python

## Installation

```bash
poetry add sitri
```

or

```bash
pip3 install sitri
```

## Basics with SystemProvider

```python
from sitri.providers.contrib import SystemConfigProvider
from sitri import Sitri

conf = Sitri(
    config_provider=SystemConfigProvider(prefix="basics"),
)
```

System provider use system environment for get config data. For unique
-sitri lookup to "namespace" by prefix.

Example:

*In console:*

```bash
export BASICS_NAME=Huey
```

*In code:*

```python
name = conf.get_config("name")

print(name)  # output: Huey
```

![Sitri](docs/_static/logo.gif#center)

#  Sitri Configuration Library

Sitri - library for managing authorization and configuration data from a single object with possibly different or identical providers

#  Installation

```bash
poetry add sitri
```

or
```bash
pip3 install sitri
```

# Basics with SystemProvider

```python
from sitri.contrib.system import SystemCredentialProvider, SystemConfigProvider
from sitri import Sitri

conf = Sitri(config_provider=SystemConfigProvider(project_prefix="basics"),
             credential_provider=SystemCredentialProvider(project_prefix="basics"))
```
System provider use system environment for get config and credential data. For unique sitri lookup to "namespace" by project_prefix.

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

#  Docs
Read base API references and other part documentation on https://sitri.readthedocs.io/

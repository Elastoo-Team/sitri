# Getting Started


## Installation

Install Sitri with Poetry (**recommend**):

```bash
poetry add sitri -E "all"
```

Install Sitri with pip:

```bash
pip install sitri[all]
```

*Extras* packs and providers:

> 1.  all - all providers and settings module.
> 2.  settings - pydantic, providers with settings-support.
> 3.  redis - for redis provider.
> 4.  hvac - for HashiCorp Vault provider.
> 5.  vedis - for vedis provider.
> 6.  pyyaml - for YAML provider.

## Basic Usage

Basic usage example with System providers (without provider
requirements):

In console:

```bash
export TEST_HOST=example.com
export TEST_PASSWORD=123
```

In code:

```python
from sitri.contrib.system import SystemConfigProvider
from sitri import Sitri

conf = Sitri(
    config_provider=SystemConfigProvider(prefix="test"),
)


print(conf.get_config("host"))
# Output: example.com

print(conf.config.keys())
# Output: ["host", "password"]
```

Note

Last output: \[\"host\", \"password\"\]

Not bug, but future. This behavior is due to the fact that in our
example we use providers with the same backend (system environment) and
same prefixes for variables (test)

Note

All kwargs in get\_config call pipe to get in provider

## Config Providers

Hint

In this section most part providers require additional libraries.
Install instruction for install dependencies in \"Prepare\" subsections.

All providers will be considered separately without Sitri class


<p align="center">
  <a href="https://github.com/elastoo-team/sitri">
    <img src="docs/_static/logo.gif">
  </a>
  <h1 align="center">
    Sitri Configuration Library
  </h1>
</p>

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FElastoo-Team%2Fsitri%2Fbadge&style=popout)](https://actions-badge.atrox.dev/Elastoo-Team/sitri/goto)
[![codecov](https://codecov.io/gh/Elastoo-Team/sitri/branch/master/graph/badge.svg)](https://codecov.io/gh/elastoo-team/sitri)
![PyPI](https://img.shields.io/pypi/v/sitri)
![Read the Docs](https://img.shields.io/readthedocs/sitri)
[![CodeFactor](https://www.codefactor.io/repository/github/elastoo-team/sitri/badge)](https://www.codefactor.io/repository/github/elastoo-team/sitri)
[![Maintainability](https://api.codeclimate.com/v1/badges/625f1d869adbf4128f75/maintainability)](https://codeclimate.com/github/Elastoo-Team/sitri/maintainability)

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
from sitri.providers.contrib import SystemConfigProvider
from sitri import Sitri

conf = Sitri(
    config_provider=SystemConfigProvider(prefix="basics"),
)
```
System provider use system environment for get config data. For unique - sitri lookup to "namespace" by prefix.

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

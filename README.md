<p align="center">
  <a href="https://github.com/elastoo-team/sitri">
    <img src="https://raw.githubusercontent.com/Elastoo-Team/sitri/master/docs/_static/full_logo.jpg">
  </a>
  <h1 align="center">
    Sitri - powerful settings & configs for python
  </h1>
</p>

[![PyPI](https://img.shields.io/pypi/v/sitri)](https://pypi.org/project/sitri/)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/sitri)](https://pypi.org/project/sitri/)
[![codecov](https://codecov.io/gh/Elastoo-Team/sitri/branch/master/graph/badge.svg)](https://codecov.io/gh/elastoo-team/sitri)
[![Maintainability](https://api.codeclimate.com/v1/badges/625f1d869adbf4128f75/maintainability)](https://codeclimate.com/github/Elastoo-Team/sitri/maintainability)
![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/Elastoo-Team/sitri)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FElastoo-Team%2Fsitri%2Fbadge&style=popout)](https://actions-badge.atrox.dev/Elastoo-Team/sitri/goto)
[![Read the Docs](https://img.shields.io/readthedocs/sitri)](https://sitri.readthedocs.io)

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

.. _getting_started:

Getting Started
===============

Installation
------------

Install Sitri with Poetry (**recommend**):

.. code-block:: sh

    poetry add sitri -E "all"

Install Sitri with pip:

.. code-block:: sh

    pip install sitri[all]

*Extras* packs and providers:

    1. all - all providers and settings module.
    2. settings - pydantic, providers with settings-support.
    3. redis - for redis provider.
    4. hvac - for HashiCorp Vault provider.
    5. vedis - for vedis provider.
    6. pyyaml - for YAML provider.


Basic Usage
------------

Basic usage example with System providers (without provider requirements):

In console:

.. code-block:: sh

    export TEST_HOST=example.com
    export TEST_PASSWORD=123

In code:

.. code-block:: python

    from sitri.contrib.system import SystemConfigProvider
    from sitri import Sitri

    conf = Sitri(
        config_provider=SystemConfigProvider(prefix="test"),
    )


    print(conf.get_config("host"))
    # Output: example.com

    print(conf.config.keys())
    # Output: ["host", "password"]

.. note::
    Last output: ["host", "password"]

    Not bug, but future. This behavior is due to the fact that in our example we use providers with the same backend (system environment) and same prefixes for variables (test)

.. note::
    All kwargs in get_config call pipe to get in provider

Config Providers
---------------------

.. hint::
    In this section most part providers require additional libraries. Install instruction for install dependencies in "Prepare" subsections.

    All providers will be considered separately without Sitri class

JSON
~~~~~~
.. include:: getting_started/providers/json.rst

YAML
~~~~~~
.. include:: getting_started/providers/yaml.rst

Redis
~~~~~~
.. include:: getting_started/providers/redis.rst

Vedis
~~~~~~
.. include:: getting_started/providers/vedis.rst

INI
~~~~~~
.. include:: getting_started/providers/ini.rst

Vault
~~~~~~
Vault KV
*********
.. include:: getting_started/providers/vault_kv.rst

For own provider
----------------
If you want write own config provider use base classes for this: :class:`ConfigProvider <sitri.config.providers.ConfigProvider>`

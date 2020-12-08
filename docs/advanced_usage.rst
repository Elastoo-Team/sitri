.. _advanced_usage:

Advanced Usage
===============

Strategy
------------

.. note::
    Strategies help you perform operations on multiple providers

Single
~~~~~~~

Basic strategy with one provider. Proxy on each other provider for Sitri class.

.. note::
    Before code with basic usage, I export variable:

        PROJECT_A=1

Example:

.. code-block:: python

    from sitri.strategy.single import SingleStrategy
    from sitri.contrib.system import SystemConfigProvider

    conf = SystemConfigProvider(prefix="project")
    strategy = SingleStrategy(conf)

    print(strategy.get("a"))
    # Output: 1

Index Priority
~~~~~~~~~~~~~~~

Strategy class take providers tuple and in loop requests values by key, if each other provider in tuple give response strategy pipe this, else response None.


.. note::

    In this example I create **data.json**:

        {
            "test1": "1",

            "test2": "2",

            "test3": "3"
        }

    Export three vars in env:
        PROJECT_TEST1=0

        PROJECT_TEST4=1

        PROJECT_TEST5=2

    Deploy Consul and create folder **project** with three vars:
        test1 = -1

        test6 = 0

        test7 = 1

Example:

.. code-block:: python

    from consul import Consul

    from sitri.strategy.index_priority import IndexPriorityStrategy
    from sitri.contrib.system import SystemConfigProvider
    from sitri.contrib.json import JsonConfigProvider
    from sitri.contrib.consul import ConsulConfigProvider

    consul_conf = ConsulConfigProvider(folder="project/", consul_connector=lambda: Consul())

    system_conf = SystemConfigProvider(prefix="project")
    json_conf = JsonConfigProvider()

    strategy = IndexPriorityStrategy((consul_conf, json_conf, system_conf))

    strategy.get("test1")
    # Output: -1

    strategy.get("test2")
    # Output: 2

    strategy.get("test4")
    # Output: 1

Settings
----------
Vault Settings Configurators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vault KV Setting Example
""""""""""""""""""""""""""

.. code-block:: python

    import hvac

    from pydantic import Field, BaseModel

    from sitri.settings.contrib.vault import VaultKVSettings
    from sitri.providers.contrib.vault import VaultKVConfigProvider
    from sitri.providers.contrib.system import SystemConfigProvider

    configurator = SystemConfigProvider(prefix="superapp")
    ENV = configurator.get("env")


    def vault_client_factory() -> hvac.Client:
        client = hvac.Client(url=configurator.get("vault_api"))

        client.auth_approle(
            role_id=configurator.get("role_id"),
            secret_id=configurator.get("secret_id"),
        )

        return client


    provider = VaultKVConfigProvider(
        vault_connector=vault_client_factory, mount_point=f"superapp/{ENV}"
    )


    class DBSettings(VaultKVSettings):
        url: str = Field(...)
        password: str = Field(...)

        class Config:
            provider = provider
            default_secret_path = "db"


    class AppSettings(BaseModel):
        db: DBSettings = Field(default_factory=DBSettings)

    settings = AppSettings()

    print(settings.dict()) # -> {'db': {'url': 'psql://test', 'password': 'testpassword'}}

.. note::
    For pydantic Field added three extra args: \

    - vault_secret_path - for secret path configuration on field level
    - vault_mount_point - for secrets mount point configuration on field level
    - vault_secret_key - for secret key configuration if secret key not equal field name

    For inside Config class added two optional fields:\

    - default_secret_path - for default secret path on all fields of setting model
    - default_mount_point - for default secrets mount path on all fields of setting model

    Secret path prioritization:

    1. vault_secret_path (Field arg)
    2. default_secret_path (Config class field)
    3. secret_path (provider initialization optional arg)

    Mount point prioritization:

    1. vault_mount_point (Field arg)
    2. default_mount_point (Config class field)
    3. mount_point (provider initialization optional arg)

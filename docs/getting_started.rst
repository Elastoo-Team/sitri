.. _getting_started:

Getting Started
===============

Installation
------------

.. attention::
    Sitri works only on Python 3.7 or higher.

    When support will for older Python versions? - Never.

Install Sitri with Poetry (**recommend**):

.. code-block:: sh

    poetry add sitri

Install Sitri with pip:

.. code-block:: sh

    pip install sitri

Install Sitri with pipenv:

.. code-block:: sh

    pipenv install sitri


Basic Usage
------------

Basic usage example with System providers (without provider requirements):

In console:

.. code-block:: sh

    export TEST_HOST=example.com
    export TEST_PASSWORD=123

In code:

.. code-block:: python

    from sitri.contrib.system import SystemConfigProvider, SystemCredentialProvider
    from sitri import Sitri

    conf = Sitri(config_provider=SystemConfigProvider(prefix="test"),
                credential_provider=SystemCredentialProvider(prefix="test"))


    print(conf.get_config("host"), conf.get_credential("password"))
    # Output: example.com 123

    print(conf.config.keys())
    # Output: ["host", "password"]

.. note::
    Last output: ["host", "password"]

    Not bug, but future. This behavior is due to the fact that in our example we use providers with the same backend (system environment) and same prefixes for variables (test)

Contribute Providers
---------------------

.. note::
    In this section most part providers require additional libraries. Install instruction for install dependencies in "Prepare" subsections

Consul
~~~~~~

Prepare
*******
.. note::
    The configuration and start of the Consul remains at your side

Install Consul client with Poetry:

.. code-block:: sh

    poetry add python-consul

Usage
******

.. note::
    :class:`ConsulConfigProvider <sitri.contrib.consul.ConsulConfigProvider>` search variables in a certain folder (default - "sitri/").

    In this example I create folder "test/" with two vars: "a" = 1 and "b" = 2

    For stub credential provider we use :class:`SystemCredentialProvider <sitri.contrib.system.SystemCredentialProvider>`

.. code-block:: python

    from consul import Consul

    from sitri.contrib.system import SystemCredentialProvider
    from sitri.contrib.consul import ConsulConfigProvider
    from sitri import Sitri

    consul = Consul()

    conf = Sitri(config_provider=ConsulConfigProvider(folder="test/", consul_connection=consul),
                credential_provider=SystemCredentialProvider(prefix="test"))

    print(conf.get_config("a"), conf.get_config("b"))
    # Output: 1 2


Redis
~~~~~~

Prepare
*******
.. note::
    The configuration and start of the Redis remains at your side

Install Consul client with Poetry:

.. code-block:: sh

    poetry add redis

Usage
******

.. note::
    :class:`RedisConfigProvider <sitri.contrib.redis.RedisConfigProvider>` and :class:`RedisCredentialProvider <sitri.contrib.redis.RedisCredentialProvider>`  search variables by prefix (as a system providers).

    In this example I export two vars:
        TEST_CONFIG_A = 1

        TEST_CREDENTIAL_A = 2


.. code-block:: python

    from redis import Redis

    from sitri.contrib.redis import RedisConfigProvider, RedisCredentialProvider
    from sitri import Sitri

    redis = Redis(host='localhost', port=6379, db=0)

    conf = Sitri(config_provider=RedisConfigProvider(prefix="test_config", redis_connection=redis),
                credential_provider=RedisCredentialProvider(prefix="test_credential", redis_connection=redis))

    print(conf.get_config("a"), conf.get_credential("a"))
    # Output: 1 2

.. note::
    Here we were able to fix the "problem" that we saw in the system providers, just separated "namespaces" using different prefixes.

Vedis
~~~~~~

Prepare
*******
.. note::
    The configuration and start of the Vedis remains at your side

Install Vedis client with Poetry:

.. code-block:: sh

    poetry add vedis

Usage
******

.. note::
    :class:`VedisConfigProvider <sitri.contrib.vedis.VedisConfigProvider>` and :class:`VedisCredentialProvider <sitri.contrib.vedis.VedisCredentialProvider>`  search variables in hash object from vedis (default hash name - sitri).

    In this example I create two vars in hash:
        a = 1
        b = 2


.. code-block:: python

    from vedis import Vedis

    from sitri.contrib.vedis import VedisConfigProvider, VedisCredentialProvider
    from sitri import Sitri

    vedis = Vedis(":mem:")

    conf = Sitri(config_provider=VedisConfigProvider(hash_name="test", vedis_connection=redis),
                credential_provider=VedisCredentialProvider(hash_name="test", vedis_connection=redis))

    print(conf.get_config("a"), conf.get_credential("b"))
    # Output: 1 2

For own provider
----------------
If you want write own credential or config provider use base classes for this: :class:`CredentialProvider <sitri.credentials.providers.CredentialProvider>`, :class:`ConfigProvider <sitri.config.providers.ConfigProvider>`

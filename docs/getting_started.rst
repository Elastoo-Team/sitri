.. _getting_started:

Getting Started
===============

Installation
------------

.. attention::
    Sitri works only on Python 3.5 or higher.

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

Contribute Providers
---------------------

.. note::
    In this section most part providers require additional libraries. Install instruction for install dependencies in "Prepare" subsections.

    All providers will be considered separately without Sitri class

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

.. code-block:: python

    from consul import Consul

    from sitri.contrib.consul import ConsulConfigProvider

    conf = ConsulConfigProvider(folder="test/", consul_connector=lambda: Consul())

    print(conf.get("a"), conf.get("b"))
    # Output: 1 2

JSON
~~~~~~

Prepare
*******

For more speed this provider you can install simplejson

.. code-block:: sh

    poetry add simplejson

Usage
******

.. note::
    In this example we have *data.json*:

    .. code-block:: json

        {
           "test":{
              "test_key1":"1",
              "test_key2":"2",
              "test_key3":"3",
              "test_key4":{
                 "test_key4_1":"1",
                 "test_key4_2":"2"
              }
           },
           "test0": "0"
        }

    In JSON's providers we have two get-modes: basic and path

    Basic mode use as default python dict. If you want get value on sub (non-first) level, you should take first level dictionary by key and get values in this dict as default.

    Path-mode make easy work with nested dictionary. You can type separated keys of nested values. *Example: test.test_key4.test_key4_1*

.. code-block:: python

    from sitri.contrib.json import JsonConfigProvider


    conf = JsonConfigProvider(json_path="./data.json", default_separator="/")

    conf.get("test.test_key1", ":(")
    # Output: :(

    conf.get("test.test_key1", ":(", path_mode=True)
    # Output: :(

    conf.get("test.test_key1", ":(", path_mode=True, separator=".")
    # Output: 1

    conf.get("test/test_key1", ":(", path_mode=True)
    # Output: 1

    conf.get("test0")
    # Output: 0

YAML
~~~~~~

Prepare
*******

**Just relax**

Usage
******

.. note::
    In this example we have *data.yaml*:

    .. code-block:: yaml

        test:
          test_key1: '1'
          test_key2: '2'
          test_key3: '3'
          test_key4:
            test_key4_1: '1'
            test_key4_2: '2'
        test0: '0'



    In YAML's providers we have two get-modes: basic and path

    Basic mode use as default python dict. If you want get value on sub (non-first) level, you should take first level dictionary by key and get values in this dict as default.

    Path-mode make easy work with nested dictionary. You can type separated keys of nested values. *Example: test.test_key4.test_key4_1*

.. code-block:: python

    from sitri.contrib.yaml import YamlConfigProvider


    conf = YamlConfigProvider(yaml_path="./data.yaml", default_separator="/")

    conf.get("test.test_key1", ":(")
    # Output: :(

    conf.get("test.test_key1", ":(", path_mode=True)
    # Output: :(

    conf.get("test.test_key1", ":(", path_mode=True, separator=".")
    # Output: 1

    conf.get("test/test_key1", ":(", path_mode=True)
    # Output: 1

    conf.get("test0")
    # Output: 0

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
    :class:`RedisConfigProvider <sitri.contrib.redis.RedisConfigProvider>` search variables by prefix (as a system providers).

    In this example I set two vars:
        TEST_CONFIG_A = 1


.. code-block:: python
    from redis import Redis

    from sitri.contrib.redis import RedisConfigProvider


    conf = RedisConfigProvider(
        prefix="test_config",
        redis_connector=lambda: Redis(host="localhost", port=6379, db=0),
    )

    print(conf.get("a"))
    # Output: 1

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
    :class:`VedisConfigProvider <sitri.contrib.vedis.VedisConfigProvider>`  search variables in hash object from vedis (default hash name - sitri).

    In this example I create two vars in hash:
        a = 1
        b = 2


.. code-block:: python

    from vedis import Vedis

    from sitri.contrib.vedis import VedisConfigProvider

    conf = VedisConfigProvider(hash_name="test", vedis_connector=lambda: Vedis(":mem:"))

    print(conf.get("a"))
    # Output: 1

For own provider
----------------
If you want write own config provider use base classes for this: :class:`ConfigProvider <sitri.config.providers.ConfigProvider>`

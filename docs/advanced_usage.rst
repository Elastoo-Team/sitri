.. _advanced_usage:

Advanced Usage
===============

Strategy
------------

.. note::
    Strategies help you perform operations on multiple providers (config or credential)

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

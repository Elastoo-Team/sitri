
Prepare
*******
.. note::
    The configuration and start of the Consul remains at your side

Install Consul client with Poetry:

.. code-block:: sh

    poetry add python-consul

Usage
******

.. hint::
    :class:`ConsulConfigProvider <sitri.contrib.consul.ConsulConfigProvider>` search variables in a certain folder (default - "sitri/").

    In this example I create folder "test/" with two vars: "a" = 1 and "b" = 2

.. code-block:: python

    from consul import Consul

    from sitri.contrib.consul import ConsulConfigProvider

    conf = ConsulConfigProvider(folder="test/", consul_connector=lambda: Consul())

    print(conf.get("a"), conf.get("b"))
    # Output: 1 2

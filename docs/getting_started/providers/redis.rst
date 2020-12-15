
Prepare
*******
.. note::
    The configuration and start of the Redis remains at your side

Install Consul client with Poetry:

.. code-block:: sh

    poetry add redis

Usage
******

.. hint::
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

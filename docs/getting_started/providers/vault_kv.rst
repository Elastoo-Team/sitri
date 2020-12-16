
Prepare
++++++++
.. note::
    The configuration and start of the Vault remains at your side


Install Vault client library with Poetry:

.. code-block:: sh

    poetry add hvac

Usage
++++++

.. hint::
    test_kv/test - secret:

    .. code-block:: json

        {
            "key1": "value1",
            "key2": "value2"
        }


Example with AppRole authenticate:

.. code-block:: python

    import hvac

    from sitri.providers.contrib.vault import VaultKVConfigProvider
    from sitri.providers.contrib.system import SystemConfigProvider

    configurator = SystemConfigProvider(prefix="test")

    def vault_client_factory() -> hvac.Client:
        client = hvac.Client(url=configurator.get("vault_api"))

        client.auth_approle(
            role_id=configurator.get("role_id"),
            secret_id=configurator.get("secret_id"),
        )

        return client

    provider = VaultKVConfigProvider(
        vault_connector=vault_client_factory,
        mount_point=f"test_kv/",
        secret_path="test"
    )

    print(provider.get("key1"))
    # Output: value1

    print(provider.get("key2"))
    # Output: value2

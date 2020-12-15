
Local is a mode for settings configurators that use an external service to get a configuration data and in local development it is more convenient to use a switch to a different provider and with the same set of fields.

Here I will give an example of using local mode in VaultKVSettings.

Let's say we have the following configuration:

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
        name: str = Field(...)

        class Config:
            provider = provider
            default_secret_path = "db"

And in a local-development environment, we don't want to deploy Vault, then we can use regular json, for example in file *config.json*:

.. code-block:: json

    {
      "db": {
        "url": "psql://localhost",
        "name": "testdb"
      }
    }

Next, we just need to add the class of our settings to the config, the fields necessary to use the local mode:

.. code-block:: python

    is_local_mode = ENV == "local"
    local_mode_filepath = configurator.get("local_mode_file_path")  # export SUPERAPP_LOCAL_MODE_FILE_PATH=/path/to/config.json

    class BaseSettingsConfig(VaultKVSettings.VaultKVSettingsConfig):
        provider = provider

        local_mode = is_local_mode
        local_mode = local_mode
        local_provider_args = {"json_path": local_mode_filepath}

    class DBSettings(VaultKVSettings):
        url: str = Field(...)
        name: str = Field(...)

        class Config(BaseSettingsConfig):
            default_secret_path = "db"
            local_mode_path_prefix = "db"

If local_mode=True, then DBSettings lookup to json file and collect config data from it.

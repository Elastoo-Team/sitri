This settings configurator has local_mode with JsonConfigProvider.

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


    class AppSettings(BaseModel):
        db: DBSettings = Field(default_factory=DBSettings)


    settings = AppSettings()

    print(settings.dict())  # -> {'db': {'url': 'psql://test', 'name': 'testdb'}}

.. important::
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

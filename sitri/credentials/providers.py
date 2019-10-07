import typing
from abc import ABC

from ..base import BaseProvider


class CredentialProvider(ABC, BaseProvider):
    """
        Base class for credential providers
    """


class CredentialProviderManager:
    """
        Manager for childeren CredentialProvider classes
    """

    @staticmethod
    def get_by_code(code: str) -> typing.Optional[typing.Type[CredentialProvider]]:
        """Get credential provider by provider_code

            :param code: provider_code for search credential provider
            :Example:
                .. code-block:: python

                    CredentialProviderManager.get_by_code("system")

                    -> SystemCredentialProvider
        """
        for provider in CredentialProvider.__subclasses__():
            if provider.provider_code == code:
                return provider
        return None

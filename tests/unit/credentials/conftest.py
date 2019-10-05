import pytest
import typing

from sitri.credentials.providers import CredentialProviderManager


@pytest.fixture(scope="module")
def credential_manager() -> typing.Type[CredentialProviderManager]:
    return CredentialProviderManager

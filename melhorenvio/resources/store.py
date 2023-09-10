"""
    Module: store
"""
from melhorenvio.core.base import MEBase


class Store(MEBase):
    """A factory for a Store class .

    This class provides methods for managing store information in the MelhorEnvio API.

    Methods:
        all: Fetch all store information.

        create: Create a store.

        get: Get store information.

        create_address: Create an address for the given store.

        list_address: List all addresses of a store.

        create_phone: Create a phone number for the store.

        list_phone: List all phone numbers for the store.
    """

    def all(self) -> dict:
        """Fetch all store information .

        This method retrieves a list of all stores associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-lojas-do-usuario).

        Usage:
        ```python
        >>> sdk.store().all()
        ```

        Returns:
            dict: A dictionary containing detailed information about all the stores.

        """
        return self._get(uri="/api/v2/me/companies")

    def create(self, body: dict) -> dict:
        """Create a store .

        This method allows you to create a new store associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/cadastrar-loja).

        Usage:
        ```python
        >>> sdk.store().create(body=body)
        ```

        Args:
            body (dict): A dictionary containing the data needed to create the store.

        Raises:
            ValueError: If the provided 'body' is not a dictionary.

        Returns:
            dict: A dictionary containing information about the newly created store.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/companies", data=body)

    def get(self, store_id: str) -> dict:
        """Get the store information .

        This method retrieves detailed information about a specific store associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/visualizar-loja).

        Usage:
        ```python
        >>> store_id = "example_store_id"
        >>> sdk.store().get(store_id=store_id)
        ```

        Args:
            store_id (str): The unique identifier of the store you want to retrieve information about.

        Returns:
            dict: A dictionary containing detailed information about the specified store.
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}")

    def create_address(self, store_id: str, body: dict) -> dict:
        """Create an address for the given store .

        This method allows you to add a new address to a specific store associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/cadastrar-endereco-de-uma-loja).

        Usage:
        ```python
        >>> store_id = "example_store_id"
        >>> sdk.store().create_address(store_id=store_id, body=body)
        ```

        Args:
            store_id (str): The unique identifier of the store for which you want to create an address.
            body (dict): A dictionary containing the address data.

        Raises:
            ValueError: If the provided 'body' is not a dictionary.

        Returns:
            dict: A dictionary containing information about the newly created address.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")
        return self._post(uri=f"/api/v2/me/companies/{store_id}/addresses", data=body)

    def list_address(self, store_id: str) -> dict:
        """List all addresses of a store .

        This method retrieves a list of all addresses associated with a specific store associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-enderecos-de-uma-loja).

        Usage:
        ```python
        >>> store_id = "example_store_id"
        >>> sdk.store().list_address(store_id=store_id)
        ```

        Args:
            store_id (str): The unique identifier of the store for which you want to list addresses.

        Returns:
            dict: A dictionary containing information about all addresses associated with the specified store.
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}/addresses")

    def create_phone(self, store_id: str, body: dict) -> dict:
        """Create a phone for store.

        This method allows you to add a phone number to a specific store associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/cadastrar-telefones-de-uma-loja).

        Usage:
        ```python
        >>> store_id = "example_store_id"
        >>> sdk.store().create_phone(store_id=store_id, body=body)
        ```

        Args:
            store_id (str): The unique identifier of the store for which you want to create a phone number.
            body (dict): A dictionary containing the phone number data.

        Raises:
            ValueError: If the provided 'body' is not a dictionary.

        Returns:
            dict: A dictionary containing information about the newly created phone number.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")
        return self._post(uri=f"/api/v2/me/companies/{store_id}/phones", data=body)

    def list_phone(self, store_id: str) -> dict:
        """List all phone numbers for store.

        This method retrieves a list of all phone numbers associated with a specific store associated with the user's account through the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-telefones-de-uma-loja).

        Usage:
        ```python
        >>> store_id = "example_store_id"
        >>> sdk.store().list_phone(store_id=store_id)
        ```

        Args:
            store_id (str): The unique identifier of the store for which you want to list phone numbers.

        Returns:
            dict: A dictionary containing information about all phone numbers associated with the specified store.
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}/phones")

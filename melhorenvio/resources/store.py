"""
    Module: store
"""
from melhorenvio.core.base import MEBase


class Store(MEBase):
    """A factory for a Store class ."""

    def all(self) -> dict:
        """Fetch all store information .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-lojas-do-usuario).

        Examples:
            >>> sdk.store().all()

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/companies")

    def create(self, body: dict) -> dict:
        """Create a store .

        [Documentation](https://docs.melhorenvio.com.br/reference/cadastrar-loja).

        Examples:
            >>> sdk.store().create(body=body)

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/companies", data=body)

    def get(self, store_id: str) -> dict:
        """Get the store information .

        [Documentation](https://docs.melhorenvio.com.br/reference/visualizar-loja).

        Examples:
            >>> sdk.store().get(store_id=store_id)

        Args:
            store_id (str): [description]

        Returns:
            dict: [description]
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}")

    def create_address(self, store_id: str, body: dict) -> dict:
        """Create an address for the given store .

        [Documentation](https://docs.melhorenvio.com.br/reference/cadastrar-endereco-de-uma-loja).

        Examples:
            >>> sdk.store().create_address(store_id=store_id, body=body)

        Args:
            store_id (str): [description]
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")
        return self._post(uri=f"/api/v2/me/companies/{store_id}/addresses", data=body)

    def list_address(self, store_id: str) -> dict:
        """List all addresses of a store .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-enderecos-de-uma-loja).

        Examples:
            >>> sdk.store().list_address(store_id=store_id)

        Args:
            store_id (str): [description]

        Returns:
            dict: [description]
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}/addresses")

    def create_phone(self, store_id: str, body: dict) -> dict:
        """Create a phone for store.

        [Documentation](https://docs.melhorenvio.com.br/reference/cadastrar-telefones-de-uma-loja).

        Examples:
            >>> sdk.store().create_phone(store_id=store_id, body=body)

        Args:
            store_id (str): [description]
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")
        return self._post(uri=f"/api/v2/me/companies/{store_id}/phones", data=body)

    def list_phone(self, store_id: str) -> dict:
        """List all phone numbers for store.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-telefones-de-uma-loja).

        Examples:
            >>> sdk.store().list_phone(store_id=store_id)

        Args:
            store_id (str): [description]

        Returns:
            dict: [description]
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}/phones")

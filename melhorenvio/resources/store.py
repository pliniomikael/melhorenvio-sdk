"""
    Module: store
"""
from melhorenvio.core.base import MEBase


class Store(MEBase):
    """A factory for a Store class ."""

    def all(self) -> dict:
        """Fetch all store information .
        https://docs.melhorenvio.com.br/reference/listar-lojas-do-usuario

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/companies")

    def create(self, body: dict) -> dict:
        """Create a store .
        https://docs.melhorenvio.com.br/reference/cadastrar-loja

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
        https://docs.melhorenvio.com.br/reference/visualizar-loja

        Args:
            store_id (str): [description]

        Returns:
            dict: [description]
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}")

    def create_address(self, store_id: str, body: dict) -> dict:
        """Create an address for the given store .
        https://docs.melhorenvio.com.br/reference/cadastrar-endereco-de-uma-loja

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
        https://docs.melhorenvio.com.br/reference/listar-enderecos-de-uma-loja

        Args:
            store_id (str): [description]

        Returns:
            dict: [description]
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}/addresses")

    def create_phone(self, store_id: str, body: dict) -> dict:
        """Create a phone for store.
        https://docs.melhorenvio.com.br/reference/cadastrar-telefones-de-uma-loja

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
        https://docs.melhorenvio.com.br/reference/listar-telefones-de-uma-loja

        Args:
            store_id (str): [description]

        Returns:
            dict: [description]
        """
        return self._get(uri=f"/api/v2/me/companies/{store_id}/phones")

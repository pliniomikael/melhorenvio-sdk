"""
    Module: cart
"""
from melhorenvio.core.base import MEBase


class Cart(MEBase):
    """A factory for a Cart class ."""

    def create(self, body: dict) -> dict:
        """Create a new cart
        https://docs.melhorenvio.com.br/reference/inserir-fretes-no-carrinho

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/cart", data=body)

    def all(self) -> dict:
        """Get all available cart .
        https://docs.melhorenvio.com.br/reference/listar-itens-do-carrinho

        Returns:
            dict: [description]
        """

        return self._get(uri="/api/v2/me/cart")

    def get(self, order_id: str) -> dict:
        """Get the cart information for a given order .
        https://docs.melhorenvio.com.br/reference/exibir-informacoes-de-item-do-carrinho

        Args:
            order_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/cart/{order_id}")

    def remove(self, order_id: str) -> dict | None:
        """Remove a cart
        https://docs.melhorenvio.com.br/reference/remocao-de-itens-do-carrinho

        Args:
            order_id (str): [description]

        Returns:
            None
            dict: [description]
        """
        return self._delete(uri=f"/api/v2/me/cart/{order_id}")

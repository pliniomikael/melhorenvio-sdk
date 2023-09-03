"""
    Module: cart
"""
from melhorenvio.core.base import MEBase


class Cart(MEBase):
    """A factory for a Cart class ."""

    def create(self, body: dict) -> dict:
        """Create a new cart .

        [Documentation](https://docs.melhorenvio.com.br/reference/inserir-fretes-no-carrinho).

        Examples:
            >>> sdk.cart().create(body=body)

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

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-itens-do-carrinho).

        Examples:
            >>> sdk.cart().all()

        Returns:
            dict: [description]
        """

        return self._get(uri="/api/v2/me/cart")

    def get(self, order_id: str) -> dict:
        """Get the cart information for a given order .

        [Documentation](https://docs.melhorenvio.com.br/reference/exibir-informacoes-de-item-do-carrinho).

        Examples:
            >>> sdk.cart().get(order_id=order_id)

        Args:
            order_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/cart/{order_id}")

    def remove(self, order_id: str) -> dict | None:
        """Remove a cart.

        [Documentation](https://docs.melhorenvio.com.br/reference/remocao-de-itens-do-carrinho).

        Examples:
            >>> sdk.cart().remove(order_id=order_id)

        Args:
            order_id (str): [description]

        Returns:
            None
            dict: [description]
        """
        return self._delete(uri=f"/api/v2/me/cart/{order_id}")

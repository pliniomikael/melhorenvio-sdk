"""
    Module: cart
"""
from melhorenvio.core.base import MEBase


class Cart(MEBase):
    """
    A factory for a Cart class.

    This class provides methods for managing shopping carts in the MelhorEnvio API.

    Methods:
        create: Create a new cart.

        all: Get all available carts.

        get: Get cart information for a given order.

        remove: Remove a cart.
    """

    def create(self, body: dict) -> dict:
        """Create a new cart .

        This method allows you to create a new cart by inserting shipping items into it using the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/inserir-fretes-no-carrinho).

        Usage:
        ```python
        >>> sdk.cart().create(body=body)
        ```

        Args:
            body (dict): A dictionary containing information about the items to be added to the cart.

        Raises:
            ValueError: If the provided request body is not a dictionary.

        Returns:
            dict: A dictionary containing information about the created cart.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/cart", data=body)

    def all(self) -> dict:
        """Get all available cart .

        This method retrieves information about all available carts in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-itens-do-carrinho).

        Usage:
        ```python
        >>> sdk.cart().all()
        ```

        Returns:
            dict: A dictionary containing information about all available carts.
        """

        return self._get(uri="/api/v2/me/cart")

    def get(self, order_id: str) -> dict:
        """Get the cart information for a given order .

        This method retrieves information about a specific cart item associated with a given order in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/exibir-informacoes-de-item-do-carrinho).

        Usage:
        ```python
        >>> order_id = "example_order_id"
        >>> sdk.cart().get(order_id=order_id)
        ```

        Args:
            order_id (str): The ID of the order for which you want to retrieve cart information.

        Returns:
            dict: A dictionary containing cart information for the specified order.
        """

        return self._get(uri=f"/api/v2/me/cart/{order_id}")

    def remove(self, order_id: str) -> dict | None:
        """Remove a cart.

        This method allows you to remove a cart item associated with a given order in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/remocao-de-itens-do-carrinho).

        Usage:
        ```python
        >>> order_id = "example_order_id"
        >>> sdk.cart().remove(order_id=order_id)
        ```

        Args:
            order_id (str): The ID of the order for which you want to remove the cart item.

        Returns:
            None
            dict: A dictionary containing information about the removed cart item.
        """
        return self._delete(uri=f"/api/v2/me/cart/{order_id}")

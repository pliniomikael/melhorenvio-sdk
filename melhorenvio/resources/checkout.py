"""
    Module: checkout
"""
from melhorenvio.core.base import MEBase


class Checkout(MEBase):
    """
    A factory for a Checkout class.

    This class provides methods for managing checkouts of shipments in the MelhorEnvio API.

    Methods:
        create: Create a checkout of the current shipment.
    """

    def create(self, body: dict) -> dict:
        """Create a checkout of the current shipment .

        This method allows you to create a checkout for the current shipment using the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/compra-de-fretes-1).

        Usage:
        ```python
        >>> sdk.checkout().create(body=body)
        ```

        Args:
            body (dict): A dictionary containing information about the shipment to be checked out.

        Raises:
            ValueError: If the provided request body is not a dictionary.

        Returns:
            dict: A dictionary containing information about the created checkout.
        """

        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/checkout", data=body)

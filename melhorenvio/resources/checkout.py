"""
    Module: checkout
"""
from melhorenvio.core.base import MEBase


class Checkout(MEBase):
    """A factory for a Checkout class"""

    def create(self, body: dict) -> dict:
        """Create a checkout of the current shipment .

        [Documentation](https://docs.melhorenvio.com.br/reference/compra-de-fretes-1).

        Examples:
            >>> sdk.checkout().create(body=body)

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """

        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/checkout", data=body)

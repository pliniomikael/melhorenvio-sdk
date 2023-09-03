"""
    Module: quotation
"""
from melhorenvio.core.base import MEBase


class Quotation(MEBase):
    """A factory for a Quotation class ."""

    def calculate(self, body: dict) -> dict:
        """Calculate the shipment information .
        https://docs.melhorenvio.com.br/reference/calculo-de-fretes-por-produtos

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/calculate", data=body)

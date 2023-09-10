"""
    Module: quotation
"""
from melhorenvio.core.base import MEBase


class Quotation(MEBase):
    """A factory for a Quotation class

    This class provides methods for calculating shipment information in the MelhorEnvio API.

    Methods:
        calculate: Calculate shipment information.
    """

    def calculate(self, body: dict) -> dict:
        """Calculate shipment information based on provided data.

        This method calculates shipping costs and information based on the provided data in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/calculo-de-fretes-por-produtos).

        Usage:
        ```python
        >>> body = {"key": "value"}  # Replace with your shipment data
        >>> sdk.quotation().calculate(body=body)
        ```

        Args:
            body (dict): The data used for calculating the shipment. Should be a dictionary.

        Raises:
            ValueError: If the provided body is not a dictionary.

        Returns:
            dict: A dictionary containing calculated shipment information.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/calculate", data=body)

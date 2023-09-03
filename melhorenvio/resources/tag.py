"""
    Module: tag
"""
from melhorenvio.core.base import MEBase


class Tag(MEBase):
    """A factory for a Tag class ."""

    def create(self, body: dict) -> dict:
        """Create a tag .
        https://docs.melhorenvio.com.br/reference/pre-visualizacao-de-etiquetas

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/generate", data=body)

    def print_tag(self, body: dict) -> dict:
        """Print a tag .
        https://docs.melhorenvio.com.br/reference/impressao-de-etiquetas

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/print", data=body)

    def preview(self, body: dict) -> dict:
        """Preview a tag data .
        https://docs.melhorenvio.com.br/reference/pre-visualizacao-de-etiquetas

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/preview", data=body)

    def search(self, filters: dict) -> dict:
        """Search tags .
        https://docs.melhorenvio.com.br/reference/pesquisar-etiqueta

        Args:
            filters (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters to request must be a Dictionary")

        return self._get(uri="/api/v2/me/orders/search", filters=filters)

    def list(self, filters: dict | None) -> dict:
        """Retrieve tags .
        https://docs.melhorenvio.com.br/reference/listar-etiquetas

        Args:
            filters (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if filters and not isinstance(filters, dict):
            raise ValueError("Filters to request must be a Dictionary")

        return self._get(uri="/api/v2/me/orders", filters=filters)

    def get(self, order_id: str) -> dict:
        """Calling the tag information  .
        https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-etiqueta

        Args:
            order_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/orders/{order_id}")

    def can_cancel(self, body: dict) -> dict:
        """Check if the tag can cancel or not .
        https://docs.melhorenvio.com.br/reference/verificar-se-etiqueta-pode-ser-cancelada

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/cancellable", data=body)

    def cancel(self, body: dict) -> dict:
        """Cancel a tag .
        https://docs.melhorenvio.com.br/reference/cancelamento-de-etiquetas

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/cancel", data=body)

    def tracking(self, body: dict) -> dict:
        """The tracking a tag for the shipment .
        https://docs.melhorenvio.com.br/reference/rastreio-de-envios

        Args:
            body (dict): [description]

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/tracking", data=body)

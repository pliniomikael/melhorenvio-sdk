"""
    Module: tag
"""
from melhorenvio.core.base import MEBase


class Tag(MEBase):
    """A factory for a Tag class .

    This class provides methods for managing shipping tags in the MelhorEnvio API.

    Methods:
        create: Create a shipping tag.

        print_tag: Print a shipping tag.

        preview: Preview shipping tag data.

        search: Search for shipping tags.

        list: List shipping tags.

        get: Retrieve information about a specific shipping tag.

        can_cancel: Check if a shipping tag can be canceled.

        cancel: Cancel a shipping tag.

        tracking: Track a shipment associated with a shipping tag.
    """

    def create(self, body: dict) -> dict:
        """Create a shipping tag.

        This method allows you to create a shipping tag for a shipment.

        [Documentation](https://docs.melhorenvio.com.br/reference/pre-visualizacao-de-etiquetas).

        Usage:
        ```python
        >>> sdk.tag().create(body=body)
        ```

        Args:
            body (dict): A dictionary containing the required information for creating the tag.

        Raises:
            ValueError: If 'body' is not a valid dictionary.

        Returns:
            dict: A dictionary containing information about the created shipping tag.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/generate", data=body)

    def print_tag(self, body: dict) -> dict:
        """Print a shipping tag.

        This method allows you to print a shipping tag for a previously generated shipment.

        [Documentation](https://docs.melhorenvio.com.br/reference/impressao-de-etiquetas).

        Usage:
        ```python
        >>> sdk.tag().print_tag(body=body)
        ```

        Args:
            body (dict): A dictionary containing the necessary information for printing the tag.

        Raises:
            ValueError: If 'body' is not a valid dictionary.

        Returns:
            dict: A dictionary containing information about the printed shipping tag.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/print", data=body)

    def preview(self, body: dict) -> dict:
        """Preview shipping tag data.

        This method allows you to preview the data for a shipping tag before generating it.

        [Documentation](https://docs.melhorenvio.com.br/reference/pre-visualizacao-de-etiquetas).

        Usage:
        ```python
        >>> sdk.tag().preview(body=body)
        ```

        Args:
            body (dict): A dictionary containing the required information for tag preview.

        Raises:
            ValueError: If 'body' is not a valid dictionary.

        Returns:
            dict: A dictionary containing the previewed shipping tag data.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/preview", data=body)

    def search(self, filters: dict) -> dict:
        """Search for shipping tags.

        This method allows you to search for shipping tags based on specific filters.

        [Documentation](https://docs.melhorenvio.com.br/reference/pesquisar-etiqueta).

        Usage:
        ```python
        >>> sdk.tag().search(filters=filters)
        ```

        Args:
            filters (dict): A dictionary containing the filtering criteria.

        Raises:
            ValueError: If 'filters' is not a valid dictionary.

        Returns:
            dict: A dictionary containing the shipping tags that match the provided filters.
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters to request must be a Dictionary")

        return self._get(uri="/api/v2/me/orders/search", filters=filters)

    def list(self, filters: dict | None) -> dict:
        """Retrieve shipping tags.

        This method allows you to retrieve shipping tags based on specific filters if provided.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-etiquetas).

        Usage:
        ```python
        >>> sdk.tag().list(filters=filters)
        ```

        Args:
            filters (dict | None): An optional dictionary containing filtering criteria, or None for no filters.

        Raises:
            ValueError: If 'filters' is not a valid dictionary.

        Returns:
            dict: A dictionary containing the shipping tags that match the provided filters or all available tags if no filters are provided.
        """
        if filters and not isinstance(filters, dict):
            raise ValueError("Filters to request must be a Dictionary")

        return self._get(uri="/api/v2/me/orders", filters=filters)

    def get(self, order_id: str) -> dict:
        """Retrieve information about a shipping tag.

        This method allows you to retrieve detailed information about a specific shipping tag using its unique order ID.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-etiqueta).

        Usage:
        ```python
        >>> sdk.tag().get(order_id=order_id)
        ```

        Args:
            order_id (str): The unique identifier (order ID) of the shipping tag.

        Returns:
            dict: A dictionary containing detailed information about the specified shipping tag.
        """
        return self._get(uri=f"/api/v2/me/orders/{order_id}")

    def can_cancel(self, body: dict) -> dict:
        """Check if a shipping tag can be canceled.

        This method allows you to determine whether a specific shipping tag can be canceled or not based on the provided data in the request body.

        [Documentation](https://docs.melhorenvio.com.br/reference/verificar-se-etiqueta-pode-ser-cancelada).

        Usage:
        ```python
        >>> sdk.tag().can_cancel(body=body)
        ```

        Args:
            body (dict): A dictionary containing the necessary data to check if the shipping tag can be canceled.

        Raises:
            ValueError: If the provided body is not a dictionary.

        Returns:
            dict: A dictionary indicating whether the shipping tag can be canceled or not, along with additional information.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/cancellable", data=body)

    def cancel(self, body: dict) -> dict:
        """Cancel a shipping tag.

        This method allows you to cancel a specific shipping tag based on the provided data in the request body.

        [Documentation](https://docs.melhorenvio.com.br/reference/cancelamento-de-etiquetas).

        Usage:
        ```python
        >>> sdk.tag().cancel(body=body)
        ```

        Args:
            body (dict): A dictionary containing the necessary data to cancel the shipping tag.

        Raises:
            ValueError: If the provided body is not a dictionary.

        Returns:
            dict: A dictionary indicating whether the shipping tag was successfully canceled or not, along with additional information.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/cancel", data=body)

    def tracking(self, body: dict) -> dict:
        """Track a shipment associated with a shipping tag.

        This method allows you to track the shipment associated with a specific shipping tag using the provided tracking data.

        [Documentation](https://docs.melhorenvio.com.br/reference/rastreio-de-envios).

        Usage:
        ```python
        >>> sdk.tag().tracking(body=body)
        ```

        Args:
            body (dict): A dictionary containing the necessary tracking data for the shipment.

        Raises:
            ValueError: If the provided body is not a dictionary.

        Returns:
            dict: A dictionary containing tracking information for the shipment associated with the shipping tag.
        """
        if not isinstance(body, dict):
            raise ValueError("Body to request must be a Dictionary")

        return self._post(uri="/api/v2/me/shipment/tracking", data=body)

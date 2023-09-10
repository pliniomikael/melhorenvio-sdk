"""
Module: base
"""
from json.encoder import JSONEncoder
from melhorenvio.config.config import Config
from melhorenvio.config.request_options import RequestOptions
from melhorenvio.http.http_client import HttpClient


class MEBase:
    """The base class for all Melhorenvio resources, providing a foundation for calling REST services.


    """

    def __init__(self, config: Config, is_production: bool = False) -> None:
        """Initialize the object with the token and the given configuration .

        Args:
            config (Config): An instance of the configuration class containing API settings.
            is_production (bool, optional): A flag indicating whether to use the production API (default is False).

        Note:
            The API base URL is determined based on the is_production flag. When is_production is True, the production
            API base URL is used; otherwise, the development API base URL is used.

        """
        self.config = config
        self.is_production = is_production
        self.request_options = RequestOptions()
        self.http_client = HttpClient()

        if self.is_production:
            self.config.api_base_url = self.config._api_base_url_prod
        else:
            self.config.api_base_url = self.config._api_base_url_dev

    def __check_headers(self, extra_headers: dict | None = None) -> dict:
        """Check and assemble the headers for an HTTP request.

        Args:
            extra_headers (dict, optional): Additional headers to include in the request (default is None).

        Returns:
            dict: A dictionary containing the assembled HTTP headers.
        """
        headers = self.request_options.get_headers(config=self.config)

        if extra_headers is not None:
            headers.update(extra_headers)

        return headers

    def _get(self, uri: str, filters: dict | None = None) -> dict | ValueError:
        """Perform a GET request to the specified URI.

        Args:
            uri (str): The URI to send the GET request to.
            filters (dict, optional): Query parameters to include in the request (default is None).

        Raises:
            ValueError: If 'filters' is provided and is not a dictionary.

        Returns:
            dict: The response data if the request is successful.
            ValueError: If the request fails or encounters an error.
        """
        if filters is not None and not isinstance(filters, dict):
            raise ValueError("Filters must be a Dictionary")

        return self.http_client.get(
            url=self.config.api_base_url + uri,
            params=filters,
            headers=self.__check_headers({"Content-type": self.config.mime_json}),
            timeout=self.request_options.connection_timeout,
            maxretries=self.request_options.max_retries,
        )

    def _post(self, uri: str, data: dict, params: str | None = None) -> dict:
        """Perform an HTTP POST request to the specified URI.

        Args:
            uri (str): The URI to send the POST request to.
            data (dict): The data to include in the POST request body.
            params (str, optional): Query parameters to include in the request (default is None).

        Returns:
            dict: The response data if the POST request is successful.
        """
        data = JSONEncoder().encode(data)

        return self.http_client.post(
            url=self.config.api_base_url + uri,
            data=data,
            params=params,
            headers=self.__check_headers({"Content-type": self.config.mime_json}),
            timeout=self.request_options.connection_timeout,
            maxretries=self.request_options.max_retries,
        )

    def _delete(self, uri:str) -> dict | None:
        """Perform an HTTP DELETE request to the specified URI.

        Args:
            uri (str): The URI to send the DELETE request to.

        Returns:
            dict | None: The response data if the DELETE request is successful. Returns None if the operation is unsuccessful.
        """
        return self.http_client.delete(
            url=self.config.api_base_url + uri,
            headers=self.__check_headers({"Content-type": self.config.mime_json}),
            timeout=self.request_options.connection_timeout,
            maxretries=self.request_options.max_retries,
        )

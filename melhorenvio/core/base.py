"""
Module: base
"""
from json.encoder import JSONEncoder
from melhorenvio.config.config import Config
from melhorenvio.config.request_options import RequestOptions
from melhorenvio.http.http_client import HttpClient


class MEBase:
    """All melhorenvio.resources extends this one to call the REST services."""

    def __init__(self, token: str, config: Config, is_production: bool = False) -> None:
        """Initialize the object with the token and the given configuration .

        Args:
            token (str): [description]
            config (Config): [description]
            is_production (bool, optional): [description]. Defaults to False.
        """
        self.token = token
        self.config = config
        self.is_production = is_production
        self.request_options = RequestOptions()
        self.http_client = HttpClient()

        if self.is_production:
            self.config.api_base_url = self.config._api_base_url_prod

        self.config.api_base_url = self.config._api_base_url_dev
        self.config.token = self.token
        self.token = None

    def __check_headers(self, extra_headers: dict | None = None) -> dict:
        """Check headers and return a dict of headers .

        Args:
            extra_headers (dict, optional): [description]. Defaults to None.

        Returns:
            dict: [description]
        """
        headers = self.request_options.get_headers(config=self.config)

        if extra_headers is not None:
            headers.update(extra_headers)

        return headers

    def _get(self, uri: str, filters: dict | None = None) -> dict | ValueError:
        """Perform a GET request .

        Args:
            uri (str): [description]
            filters (dict, optional): [description]. Defaults to None.

        Raises:
            ValueError: [description]

        Returns:
            dict: [description]
            ValueError: [description]
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
        """Perform a POST request .

        Args:
            uri (str): [description]
            data (dict): [description]
            params (str, optional): [description]. Defaults to None.

        Returns:
            dict: [description]
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

    def _delete(self, uri) -> dict | None:
        """HTTP DELETE method .

        Returns:
            [type]: [description]
        """
        return self.http_client.delete(
            url=self.config.api_base_url + uri,
            headers=self.__check_headers({"Content-type": self.config.mime_json}),
            timeout=self.request_options.connection_timeout,
            maxretries=self.request_options.max_retries,
        )

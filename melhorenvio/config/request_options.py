"""
Module: request_options
"""
from melhorenvio.config import Config


class RequestOptions:
    """Configuration options for making REST API requests.

    This class holds configuration settings that affect the behavior of REST API requests.

    Methods:
        get_headers: Generates and returns the HTTP headers to be included in the request, including the Authorization header.

    """

    def __init__(self, connection_timeout: float = 60.0, max_retries: int = 3):
        """Initialize the RequestOptions object with connection timeout and maximum retries.

        Args:
            connection_timeout (float, optional): The maximum time, in seconds, to wait for a request to establish a connection. Defaults to 60.0.
            max_retries (int, optional): The maximum number of retries to attempt for a failed request. Defaults to 3.
        """

        self.connection_timeout = connection_timeout
        self.max_retries = max_retries

    def get_headers(self, config: Config) -> dict:
        """Generate HTTP headers for the request, including the Authorization header.

        Args:
            config (Config): The configuration object that holds authentication information.

        Returns:
            dict: A dictionary of HTTP headers to be included in the request.
        """

        headers = {
            "Authorization": "Bearer " + config.token,
            "User-Agent": config.user_agent,
            "Accept": config.mime_json,
        }

        return headers

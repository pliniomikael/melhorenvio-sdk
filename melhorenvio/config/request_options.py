"""
Module: request_options
"""
from melhorenvio.config import Config


class RequestOptions:
    """This object hold all configurations that will be used in ur REST call.

    All here u can customize as well add params in the requisition header (custom_headers)
    """

    def __init__(self, connection_timeout: float = 60.0, max_retries: int = 3):
        """Initialize the class .

        Args:
            connection_timeout (float, optional): [description]. Defaults to 60.0.
            max_retries (int, optional): [description]. Defaults to 3.


        """
        self.connection_timeout = connection_timeout
        self.max_retries = max_retries

    def get_headers(self, config: Config) -> dict:
        """Add Authorization header to the request .
        Args:
            config (Config): [description]

        Returns:
            dict: [description]
        """

        headers = {
            "Authorization": "Bearer " + config.token,
            "User-Agent": config.user_agent,
            "Accept": config.mime_json,
        }

        return headers

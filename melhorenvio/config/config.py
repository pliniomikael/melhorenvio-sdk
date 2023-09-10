"""
Module: config
"""


class Config:
    """Configuration settings for your SDK.

    This class holds the configuration settings required for your SDK to communicate with the API.
    """

    def __init__(
        self,
        user_agent: str,
        client_id: int,
        client_secret: str,
        redirect_uri: str,
        code: str,
    ) -> None:
        """Initialize the configuration object for the SDK client.

        Args:
            user_agent (str): The user agent string to identify your SDK.
            client_id (int): The client ID provided for your application.
            client_secret (str): The client secret provided for your application.
            code (str): The authorization code or access token used for API requests.
            redirect_uri (str): The redirect URI used for authentication.
        """
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token: str = code
        self.api_base_url: str = ""
        self._api_base_url_prod: str = "https://melhorenvio.com.br"
        self._api_base_url_dev: str = "https://sandbox.melhorenvio.com.br"
        self.mime_json: str = "application/json"
        self.mime_form: str = "application/x-www-form-urlencoded"

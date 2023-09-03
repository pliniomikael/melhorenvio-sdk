"""
Module: config
"""


class Config:
    """
    General infos of your SDK
    """

    def __init__(
        self,
        user_agent: str,
        client_id: int,
        client_secret: str,
        redirect_uri: str,
        code: str,
    ) -> None:
        """Initialize the object to be used for the client .

        Args:
            user_agent (str): [description]
            client_id (int): [description]
            client_secret (str): [description]
            code (str): [description]
            redirect_uri (str): [description]


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

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
        client_name: str,
        client_email: str,
        client_id: int,
        client_secret: str,
        redirect_uri: str,
    ) -> None:
        """Initialize the object to be used for the client .

        Args:
            user_agent (str): [description]
            client_name (str): [description]
            client_email (str): [description]
            client_id (int): [description]
            client_secret (str): [description]
            redirect_uri (str): [description]


        """
        self.user_agent = user_agent
        self.client_name = client_name
        self.client_email = client_email
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.api_base_url: str = ""
        self.token: str = ""
        self._api_base_url_prod: str = "https://melhorenvio.com.br"
        self._api_base_url_dev: str = "https://sandbox.melhorenvio.com.br"
        self.mime_json: str = "application/json"
        self.mime_form: str = "application/x-www-form-urlencoded"

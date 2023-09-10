"""
    Module: auth
"""
from melhorenvio.core.base import MEBase


class Auth(MEBase):
    """
    A factory for an Auth class.

    This class provides methods for authentication and managing app settings in the MelhorEnvio API.

    Methods:
        app_settings: Returns the current app settings.

        login: Authenticate using the given code.

        refresh_token: Refresh a refresh token.

    """


    def app_settings(self) -> dict:
        """Returns the current app settings .

        This method retrieves the current application settings from the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-aplicativo) for this func.

        Usage:
        ```python
        >>> sdk.auth().app_settings()
        ```

        Returns:
            dict: A dictionary containing application settings.
        """
        return self._get(uri="/api/v2/me/shipment/app-settings")

    def login(self, code: str) -> dict:
        """
        Authenticate using the given code.

        This method authenticates the user by exchanging the provided code for an access token using the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/solicitacao-do-token).

        Usage:
        ```python
        >>> code = "your_auth_code"
        >>> sdk.auth().login(code=code)
        ```

        Args:
            code (str): The authentication code obtained during the OAuth2 authorization process.

        Returns:
            dict: A dictionary containing authentication information.
        """
        payload = {
            "grant_type": "authorization_code",
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "redirect_uri": self.config.redirect_uri,
            "code": code,
        }
        return self._post(uri="/oauth/token", data=payload)

    def refresh_token(self) -> dict:
        """
        Refresh a refresh token.

        This method refreshes an expired access token using a refresh token in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/solicitacao-do-token).

        Usage:
        ```python
        >>> sdk.auth().refresh_token()
        ```

        Returns:
            dict: A dictionary containing refreshed token information.
        """
        payload = {
            "grant_type": "refresh_token",
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "refresh_token": self.config.token,
        }
        return self._post(uri="/oauth/token", data=payload)

"""
    Module: auth
"""
from melhorenvio.core.base import MEBase


class Auth(MEBase):
    """A factory for a Auth class ."""

    def app_settings(self) -> dict:
        """Returns the current app settings .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-aplicativo) for this func.

        Examples:
            >>> sdk.auth().app_settings()

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/shipment/app-settings")

    def login(self, code: str) -> dict:
        """Authenticate using the given code .

        [Documentation](https://docs.melhorenvio.com.br/reference/solicitacao-do-token).

        Examples:
            >>> sdk.auth().login(code=code)

        Args:
            code (str): [description]

        Returns:
            (dict): [description]
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
        """Refresh a refresh token .

        [Documentation](https://docs.melhorenvio.com.br/reference/solicitacao-do-token).

        Examples:
            >>> sdk.auth().refresh_token()

        Returns:
            dict: [description]
        """
        payload = {
            "grant_type": "refresh_token",
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "refresh_token": self.config.token,
        }
        return self._post(uri="/oauth/token", data=payload)

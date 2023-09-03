"""
    Module: user
"""
from melhorenvio.core.base import MEBase


class User(MEBase):
    """A factory for a User class ."""

    def me(self) -> dict:
        """Returns the current user information .
        https://docs.melhorenvio.com.br/reference/listar-informacoes-do-usuario

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me")

    def addresses(self) -> dict:
        """List of addresses of current user account .
        https://docs.melhorenvio.com.br/reference/listar-enderecos-do-usuario

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/addresses")

    def balance(self) -> dict:
        """Returns the balance of the current user .
        https://docs.melhorenvio.com.br/reference/saldo-do-usuario

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/balance")

    def insert_balance(self, gateway: str, value: str) -> dict:
        """Inserts a new balance for a given gateway .
        https://docs.melhorenvio.com.br/reference/inserir-saldo-na-carteira-do-usuario

        Args:
            gateway (str): [description]
            value (str): [description]

        Returns:
            dict: [description]
        """
        return self._post(
            uri="/api/v2/me/balance",
            data={
                "gateway": gateway,
                "redirect": self.config.redirect_uri,
                "value": value,
            },
        )

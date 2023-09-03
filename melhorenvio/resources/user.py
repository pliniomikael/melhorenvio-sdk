"""
    Module: user
"""
from melhorenvio.core.base import MEBase


class User(MEBase):
    """A factory for a User class ."""

    def me(self) -> dict:
        """Returns the current user information .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-do-usuario).

        Examples:
            >>> sdk.user().me()

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me")

    def addresses(self) -> dict:
        """List of addresses of current user account .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-enderecos-do-usuario).

        Examples:
            >>> sdk.user().addresses()

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/addresses")

    def balance(self) -> dict:
        """Returns the balance of the current user .

        [Documentation](https://docs.melhorenvio.com.br/reference/saldo-do-usuario).

        Examples:
            >>> sdk.user().balance()

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/balance")

    def insert_balance(self, gateway: str, value: str) -> dict:
        """Inserts a new balance for a given gateway .

        [Documentation](https://docs.melhorenvio.com.br/reference/inserir-saldo-na-carteira-do-usuario).

        Examples:
            >>> sdk.user().insert_balance(gateway=gateway, value=value)

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

"""
    Module: user
"""
from melhorenvio.core.base import MEBase


class User(MEBase):
    """
    A factory for a User class.

    This class provides methods to interact with user information in the MelhorEnvio API.

    Methods:
        me: Returns the current user information.

        addresses: List of addresses of the current user account.

        balance: Returns the balance of the current user.

        insert_balance: Inserts a new balance for a given gateway.
    """
    def me(self) -> dict:
        """Returns the current user information .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-do-usuario).

        Usage:
        ```python
        >>> sdk.user().me()
        ```

        Returns:
            dict: A dictionary containing user information.
        """
        return self._get(uri="/api/v2/me")

    def addresses(self) -> dict:
        """List of addresses of current user account .

        This method retrieves a list of addresses associated with the current user account in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-enderecos-do-usuario).

        Usage:
        ```python
        >>> sdk.user().addresses()
        ```

        Returns:
            dict: A dictionary containing a list of user addresses.
        """
        return self._get(uri="/api/v2/me/addresses")

    def balance(self) -> dict:
        """Returns the balance of the current user .

        This method retrieves the balance of the current user's account in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/saldo-do-usuario).

        Usage:
        ```python
        >>> sdk.user().balance()
        ```

        Returns:
            dict: A dictionary containing the user's balance information.
        """
        return self._get(uri="/api/v2/me/balance")

    def insert_balance(self, gateway: str, value: str) -> dict:
        """Inserts a new balance for a given gateway .

        This method allows you to insert a new balance for a specific gateway in the user's account in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/inserir-saldo-na-carteira-do-usuario).

        Usage:
        ```python
        >>> gateway = "example_gateway"
        >>> value = "100.00"
        >>> sdk.user().insert_balance(gateway=gateway, value=value)
        ```

		Args:
			gateway (str): The gateway for which you want to insert the balance.
			value (str): The value of the balance to be inserted.

		Returns:
			dict: A dictionary containing information about the inserted balance.
		"""
        return self._post(
            uri="/api/v2/me/balance",
            data={
                "gateway": gateway,
                "redirect": self.config.redirect_uri,
                "value": value,
            },
        )

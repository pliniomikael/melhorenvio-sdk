"""
Module: sdk
"""
from melhorenvio.config.config import Config
from melhorenvio.resources import (
    Auth,
    User,
    Store,
    Company,
    Quotation,
    Tag,
    Cart,
    Checkout,
)


class SDK:
    """Generate access to all API' modules, which are:

    1. Auth
    2. User
    3. Store
    4. Company
    5. Quotation
    6. Tag
    7. Cart
    8. Checkout
    """

    def __init__(self, user_config: dict, is_production: bool = False) -> None:
        """Construct SDK Object to have access to all APIs modules .

        [Documentation for more info](https://docs.melhorenvio.com.br/reference/aplicativo-autenticacao).

        Usage:
        ```python
        >>> sdk = SDK(
        is_production=False,
        user_config={
            "user_agent": "Aplicação (email para contato técnico)",
            "client_id": 1234,
            "client_secret": "senha",
            "redirect_uri": "https://localhost.com/approve/",
            "code": "dkjahsdqoiweuqw",
            },
        )
        ```


        Args:
            user_config (dict): Information for config SDK
            is_production (bool, optional): Defaults to False.

        """
        self.is_production = is_production
        self.config = Config(
            user_config["user_agent"],
            user_config["client_id"],
            user_config["client_secret"],
            user_config["redirect_uri"],
            user_config["code"],
        )

    def auth(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.auth(). # all funcs for Auth class
        ```
        """
        return Auth(is_production=self.is_production, config=self.config)

    def user(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.user(). # all funcs for User class
        ```
        """
        return User(is_production=self.is_production, config=self.config)

    def store(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.store(). # all funcs for Store class
        ```
        """
        return Store(is_production=self.is_production, config=self.config)

    def company(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.company(). # all funcs for Company class
        ```
        """
        return Company(is_production=self.is_production, config=self.config)

    def quotation(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.quotation(). # all funcs for Quotation class
        ```
        """
        return Quotation(is_production=self.is_production, config=self.config)

    def tag(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.tag(). # all funcs for Tag class
        ```
        """
        return Tag(is_production=self.is_production, config=self.config)

    def cart(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.cart(). # all funcs for Cart class
        ```
        """
        return Cart(is_production=self.is_production, config=self.config)

    def checkout(self):
        """
        Returns the attribute value of the function

        Usage:
        ```python
        >>> sdk.checkout(). # all funcs for Checkout class
        ```
        """
        return Checkout(is_production=self.is_production, config=self.config)

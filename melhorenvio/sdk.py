"""
Module: sdk
"""
from melhorenvio.config.config import Config
from melhorenvio.resources import (
    Auth,
    Cart,
    Checkout,
    Company,
    Quotation,
    Store,
    Tag,
    User,
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

    def __init__(self, token: str, user_config: dict, is_production: bool = False) -> None:
        """Construct SDK Object to have access to all APIs modules .
        [Click here for more info](https://docs.melhorenvio.com.br/reference/aplicativo-autenticacao)
        Args:
            token (str): [description]
            user_config (dict): [description]
            is_production (bool, optional): [description]. Defaults to False.


        """
        self.token = token
        self.is_production = is_production
        self.config = Config(
            user_config["user_agent"],
            user_config["client_name"],
            user_config["client_email"],
            user_config["client_id"],
            user_config["client_secret"],
            user_config["redirect_uri"],
        )

    def auth(self):
        """
        Returns the attribute value of the function
        """
        return Auth(is_production=self.is_production, token=self.token, config=self.config)

    def user(self):
        """
        Returns the attribute value of the function
        """
        return User(is_production=self.is_production, token=self.token, config=self.config)

    def store(self):
        """
        Returns the attribute value of the function
        """
        return Store(is_production=self.is_production, token=self.token, config=self.config)

    def company(self):
        """
        Returns the attribute value of the function
        """
        return Company(is_production=self.is_production, token=self.token, config=self.config)

    def quotation(self):
        """
        Returns the attribute value of the function
        """
        return Quotation(is_production=self.is_production, token=self.token, config=self.config)

    def tag(self):
        """
        Returns the attribute value of the function
        """
        return Tag(is_production=self.is_production, token=self.token, config=self.config)

    def cart(self):
        """
        Returns the attribute value of the function
        """
        return Cart(is_production=self.is_production, token=self.token, config=self.config)

    def checkout(self):
        """
        Returns the attribute value of the function
        """
        return Checkout(is_production=self.is_production, token=self.token, config=self.config)

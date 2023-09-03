"""
Module: resources/__init__.py
"""
from melhorenvio.config.request_options import RequestOptions
from melhorenvio.http.http_client import HttpClient
from melhorenvio.resources.auth import Auth
from melhorenvio.resources.cart import Cart
from melhorenvio.resources.checkout import Checkout
from melhorenvio.resources.company import Company
from melhorenvio.resources.quotation import Quotation
from melhorenvio.resources.store import Store
from melhorenvio.resources.tag import Tag
from melhorenvio.resources.user import User


__all__ = (
    "Auth",
    "HttpClient",
    "RequestOptions",
    "Cart",
    "Checkout",
    "Company",
    "Quotation",
    "Store",
    "Tag",
    "User",
)

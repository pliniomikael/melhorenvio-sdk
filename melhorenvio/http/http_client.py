"""
Module: http_client
"""
from httpx import HTTPTransport, Client


class HttpClient:
    """
    Default implementation to call all REST API's
    """

    def request(
        self,
        method: str,
        url: str,
        maxretries: int,
        timeout: float,
        headers: dict,
        params: dict | None,
        **kwargs: dict
    ) -> dict:
        """Makes a call to the API.

        All **kwargs are passed verbatim to ``requests.request``.
        """

        with Client(transport=HTTPTransport(retries=maxretries), headers=headers, timeout=timeout) as session:
            api_result = session.request(method, url, params=params, **kwargs)
            response = {"status": api_result.status_code, "response": api_result.json()}

        return response

    def get(self, url: str, headers: dict, timeout: int, maxretries: int, params: dict | None = None) -> dict:
        """Makes a GET request to the API

        Returns:
            dict: [description]
        """
        return self.request(
            "GET",
            url=url,
            headers=headers,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def post(
        self, url: str, headers: dict, timeout: int, maxretries: int, data: dict, params: dict | None = None
    ) -> dict:
        """Makes a POST request to the API

        Returns:
            dict: [description]
        """
        return self.request(
            "POST",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def put(
        self, url: str, headers: dict, timeout: int, maxretries: int, data: dict, params: dict | None = None
    ) -> dict:
        """Makes a PUT request to the API.

        Returns:
            dict: [description]
        """
        return self.request(
            "PUT",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def delete(self, url: str, headers: dict, timeout: int, maxretries: int) -> dict | None:
        """Makes a DELETE request to the API

        Returns:
            dict: [description]
        """
        return self.request(
            "DELETE",
            url=url,
            headers=headers,
            timeout=timeout,
            maxretries=maxretries,
        )

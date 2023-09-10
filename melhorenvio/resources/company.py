"""
    Module: company
"""
from melhorenvio.core.base import MEBase


class Company(MEBase):
    """
    A factory for a Company class.

    This class provides methods for managing company and service information in the MelhorEnvio API.

    Methods:
        all_company: Gets information about all companies.

        get_company: Get details of a specific company.

        all_services: Get information about all services.

        get_service: Get details of a specific service.

        list_agencies: List all agencies with optional filters.

        get_agency: Get details of a specific agency.
    """

    def all_company(self) -> dict:
        """Get information about all companies.

        This method retrieves information about all available shipping companies in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-transportadoras).

        Usage:
        ```python
        >>> sdk.company().all_company()
        ```

        Returns:
            dict: A dictionary containing information about all available shipping companies.
        """
        return self._get(uri="/api/v2/me/shipment/companies")

    def get_company(self, company_id: str) -> dict:
        """Get details of a specific company.

        This method retrieves detailed information about a specific shipping company in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-transportadora).

        Usage:
        ```python
        >>> company_id = "example_company_id"
        >>> sdk.company().get_company(company_id=company_id)
        ```

        Args:
            company_id (str): The ID of the company for which you want to retrieve information.

        Returns:
            dict: A dictionary containing detailed information about the specified shipping company.
        """

        return self._get(uri=f"/api/v2/me/shipment/companies/{company_id}")

    def all_services(self) -> dict:
        """Get information about all services.

        This method retrieves information about all available shipping services in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-servicos).

        Usage:
        ```python
        >>> sdk.company().all_services()
        ```

        Returns:
            dict: A dictionary containing information about all available shipping services.
        """

        return self._get(uri="/api/v2/me/shipment/services")

    def get_service(self, service_id: str) -> dict:
        """Get details of a specific service.

        This method retrieves detailed information about a specific shipping service in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-um-servico).

        Usage:
        ```python
        >>> service_id = "example_service_id"
        >>> sdk.company().get_service(service_id=service_id)
        ```

        Args:
            service_id (str): The ID of the service for which you want to retrieve information.

        Returns:
            dict: A dictionary containing detailed information about the specified shipping service.
        """

        return self._get(uri=f"/api/v2/me/shipment/services/{service_id}")

    def list_agencies(self, filters: dict | None) -> dict:
        """List all agencies with optional filters.

        This method retrieves a list of all available shipping agencies with optional filtering in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-agencias-e-opcoes-de-filtro).

        Usage:
        ```python
        >>> sdk.company().list_agencies()
        >>> filters = {"key": "value"}
        >>> sdk.company().list_agencies(filters=filters)
        ```

        Args:
            filters (dict, optional): Optional filters for agency listing.

        Returns:
            dict: A dictionary containing information about shipping agencies.
        """

        return self._get(uri="/api/v2/me/shipment/agencies", filters=filters)

    def get_agency(self, agency_id: str) -> dict:
        """Get details of a specific agency.

        This method retrieves detailed information about a specific shipping agency in the MelhorEnvio API.

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-agencia).

        Usage:
        ```python
        >>> agency_id = "example_agency_id"
        >>> sdk.company().get_agency(agency_id=agency_id)
        ```

        Args:
            agency_id (str): The ID of the agency for which you want to retrieve information.

        Returns:
            dict: A dictionary containing detailed information about the specified shipping agency.
        """

        return self._get(uri=f"/api/v2/me/shipment/agencies/{agency_id}")

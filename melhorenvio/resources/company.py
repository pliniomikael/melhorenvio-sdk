"""
    Module: company
"""
from melhorenvio.core.base import MEBase


class Company(MEBase):
    """A factory for a Company class ."""

    def all_company(self) -> dict:
        """Gets all company companys  information .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-transportadoras).

        Examples:
            >>> sdk.company().all_company()

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/shipment/companies")

    def get_company(self, company_id: str) -> dict:
        """Calling company details .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-transportadora).

        Examples:
            >>> sdk.company().get_company(company_id=company_id)

        Args:
            company_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/shipment/companies/{company_id}")

    def all_services(self) -> dict:
        """Get all services .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-servicos).

        Examples:
            >>> sdk.company().all_services()

        Returns:
            dict: [description]
        """

        return self._get(uri="/api/v2/me/shipment/services")

    def get_service(self, service_id: str) -> dict:
        """Returns information about a service .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-um-servico).

        Examples:
            >>> sdk.company().get_service(service_id=service_id)

        Args:
            service_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/shipment/services/{service_id}")

    def list_agencies(self, filters: dict | None) -> dict:
        """List all agencies .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-agencias-e-opcoes-de-filtro).

        Examples:
            >>> sdk.company().list_agencies()
            >>> sdk.company().list_agencies(filters=filters)

        Args:
            filters (dict): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri="/api/v2/me/shipment/agencies", filters=filters)

    def get_agency(self, agency_id: str) -> dict:
        """Returns information about a agency .

        [Documentation](https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-agencia).

        Examples:
            >>> sdk.company().get_agency(agency_id=agency_id)

        Args:
            agency_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/shipment/agencies/{agency_id}")

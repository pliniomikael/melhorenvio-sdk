"""
    Module: company
"""
from melhorenvio.core.base import MEBase


class Company(MEBase):
    """A factory for a Company class ."""

    def all_company(self) -> dict:
        """Gets all company companys  information .
        https://docs.melhorenvio.com.br/reference/listar-transportadoras

        Returns:
            dict: [description]
        """
        return self._get(uri="/api/v2/me/shipment/companies")

    def get_company(self, company_id: str) -> dict:
        """Calling company details .
        https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-transportadora

        Args:
            company_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/shipment/companies/{company_id}")

    def all_services(self) -> dict:
        """Get all services .
        https://docs.melhorenvio.com.br/reference/listar-servicos

        Returns:
            dict: [description]
        """

        return self._get(uri="/api/v2/me/shipment/services")

    def get_service(self, service_id: str) -> dict:
        """Returns information about a service
        https://docs.melhorenvio.com.br/reference/listar-informacoes-de-um-servico

        Args:
            service_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/shipment/services/{service_id}")

    def list_agencies(self, filters: dict | None) -> dict:
        """List all agencies .
        https://docs.melhorenvio.com.br/reference/listar-agencias-e-opcoes-de-filtro

        Args:
            filters (dict): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri="/api/v2/me/shipment/agencies", filters=filters)

    def get_agency(self, agency_id: str) -> dict:
        """Returns information about a agency .
        https://docs.melhorenvio.com.br/reference/listar-informacoes-de-uma-agencia

        Args:
            agency_id (str): [description]

        Returns:
            dict: [description]
        """

        return self._get(uri=f"/api/v2/me/shipment/agencies/{agency_id}")

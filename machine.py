"""
This module defines the printer DataHandler domain.
"""

from .enterprise_BR.entity import DataHandler
from .enterprise_BR.client_repository import ClientServerInterface
from .enterprise_BR.processor_repository import DataProcessorInterface
from .enterprise_BR.validation_repository import ValidatorInterface
from typing import Literal, Any


class MachineDataHandler(DataHandler):
    """
    This class defines the DataHandler domain. In this use of case, it is connection to data generated by our
    enterprises machines.
    """

    def __init__(self, machine_id: str):
        super().__init__()
        machine_id: str = machine_id

    async def machine_fetch(self, client_server: ClientServerInterface, method: Literal["GET", "POST", "PUT", "PATCH"],
                            url: str, header: dict[str, str] | None = None,
                            body: dict[str, any] | None = None) -> list[dict[str, any]]:
        """
        Fetch data from the specified endpoint.

        :param client_server: Adapter to fetch the data.
        :type client_server: ClientServerInterface
        :param method: "GET", "POST", "PUT", "PATCH". Http methods
        :type method: Literal["GET", "POST", "PUT", "PATCH"]
        :param url: Path pointing where is the data
        :type url: str
        :param header: Correspond headers
        :type header: Dictionary
        :param body: Correspond body data if it is necessary
        :type body: dict[str, any]
        :return: Data fetch.
        :rtype: list[dict[str, any]]
        """
        return await self.fetch(client_server, method, url, header, body)

    async def machine_validator(self, validator: ValidatorInterface, response: list[dict[str, any]],
                                validation_structure: dict) -> bool:
        """
        Validate the fetched data.

        :param response: Data fetch.
        :type response: list[dict[str, any]]
        :param validator: Adapter to validate the data.
        :type validator: ValidatorInterface
        :param validation_structure: Structure to validate the response from the client server
        :type validation_structure: dict
        :return: Data correctly validated. If error return false
        :rtype: bool
        """
        return await self.validator(validator, response, validation_structure)

    async def machine_refiner(self, transform_method: type(DataProcessorInterface), response: list[dict[str, any]],
                              **kwargs) -> any:
        """
        Refine and transform the fetched data.
        
        :param response: Data fetch.
        :type response: list[dict[str, any]]
        :param transform_method: A bound method of DataProcessorInterface and returns refined
        statistical data.
        :type transform_method: Must pass a bound method for class DataProcessorInterface
        :param kwargs: Extra parameters to interact with processor data logic
        :type kwargs: Any
        :return: Data correctly validated and transformed returned in basic types format.
        :rtype: list[dict[str, any]] | dict[str, dict[str, any] | dict[str, any]]
        """
        return await self.refiner(transform_method, data=response, **kwargs)

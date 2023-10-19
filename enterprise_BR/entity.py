"""
Encapsulate Critical Business Rules.
1. Fetch for data in the right place.
2. Validate the received data.
3. Transform this data and send it to higher layers.
"""
from .client_repository import ClientServerInterface
from .processor_repository import DataProcessorInterface
from .validation_repository import ValidatorInterface
from dataclasses import dataclass
from typing import Literal, Any


@dataclass
class DataHandler:

    @staticmethod
    async def fetch(client_server: ClientServerInterface, method: Literal["GET", "POST", "PUT", "PATCH"],
                    url: str, header: dict[str, str] | None = None,
                    body: dict[str, any] | None = None) -> list[dict[str, any]]:
        """
        Fetches data from a server using the specified method and URL.

        :param client_server: An instance of ClientServerInterface used for making the request.
        :type client_server: ClientServerInterface
        :param method: The HTTP method to use for the request. Must be one of "GET", "POST", "PUT", or "PATCH".
        :type method: Literal["GET", "POST", "PUT", "PATCH"]
        :param url: The URL to fetch data from.
        :type url: str
        :param header: Optional headers to include in the request. Should be a dictionary of string keys and string
         values.
        :type header: dict[str, str] or None
        :param body: Optional request body to send with the request.
        :type body: body: dict[str, any] | None = None
        :return: A list of dictionaries representing the fetched data. Each dictionary can have keys of any string and
         values of any type.
        :rtype: list[dict[str, any]]
        """
        return await client_server.fetch(method, url, header, body)

    @staticmethod
    async def refiner(transform_method: type(DataProcessorInterface), data: list[dict[str, any]],
                      **kwargs) -> list[dict[str, any]]:
        """
        Applies a transformation method to input data and returns refined statistical output data.

        :param transform_method: A bound method of DataProcessorInterface and returns refined
         statistical data.
        :type transform_method: Must pass a bound method for class DataProcessorInterface
        :param data: Data to be transformed
        :type data: list[dict[str, any]]
        :param kwargs: Additional keyword arguments to be passed to the transform_method.
        :type kwargs: Any
        :return: Refined statistical output data.
        :rtype: list[dict[str, any]]
        """
        return await transform_method(data, **kwargs)

    @staticmethod
    async def validator(validator: ValidatorInterface, input_data: list[dict[str, any]], structure: dict) -> bool:
        """
        Validates if the data pass to the function corresponds with the desired ues case data. If not raise
        ValidationError.
        :param validator: An instance of ValidatorInterface used for validate data.
        :type validator: ValidatorInterface
        :param input_data: Input data to be validated.
        :type input_data: list[dict[str, any]]
        :param structure: The structure that describe the input data to be validated.
        :type structure: dict
        :return: Return ture if the operation succeed.
        :rtype: Boolean
        """
        return await validator.validate(input_data, structure)

from abc import ABC, abstractmethod
from typing import Any


class ValidatorInterface(ABC):
    @abstractmethod
    async def validate(self, data: list[dict[str, any]], structure: dict) -> bool:
        """
        Validates if the data pass to the function corresponds with the desired ues case data. If not raise
        ValidationError.
        :param data: Input data to be validated.
        :type data: list[dict[str, any]]
        :param structure: The structure of the input data to be validated.
        :type structure: dict
        :return: Return ture if the operation succeed.
        :rtype: Boolean
        """
        raise NotImplemented

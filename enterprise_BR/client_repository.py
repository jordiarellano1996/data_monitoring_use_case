from abc import ABC, abstractmethod
from typing import Literal


class ClientServerInterface(ABC):
    @abstractmethod
    async def fetch(self, method: Literal["GET", "POST", "PUT", "PATCH"], url: str,
                    header: dict[str, str] | None = None, body: dict[str, any] | None = None) -> list[dict[str, any]]:
        """
        Fetch data to the correspond location.
        :param method: Determine the correspond http method to use.
        :type method: Literal["GET", "POST", "PUT", "PATCH"]
        :param url: Defines URL to fetch the data.
        :type url: str
        :param header: Defines Headers to fetch the data.
        :type header: dict[str, str] | None = None
        :param body: Optional request body to send with the request.
        :type body: list[dict[str, any]]
        """
        raise NotImplemented

from abc import ABC, abstractmethod
from typing import List, Dict, Literal


class DataProcessorInterface(ABC):

    @abstractmethod
    async def down_sample(self, data: List[Dict[str, any]], group_by_key: list[str], timestamp_key: str,
                          frequency: str = "1T") -> list[dict[str, any]]:
        """
        Down samples the data to a specified frequency and returns the result as a list of dictionaries.
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: The dictionary key for data device.
        :type group_by_key: list[str]
        :param timestamp_key: The dictionary key for timestamp.
        :type timestamp_key: str
        :param frequency: The desired frequency for down sampling. Defaults to "1T".
        :type frequency: str
        :return: The down sampled data as a list of dictionaries.
        :rtype: List[Dict[str, any]]
        """
        raise NotImplemented

    @abstractmethod
    async def stats_description(self, data: List[Dict[str, any]], group_by_key: list[str],
                                target_key: str, ) -> list[dict[str, any]]:
        """
        Calculates descriptive statistics for the data and returns the result as a dictionary.
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: The dictionary key for data device.
        :type group_by_key: list[str]
        :param target_key: The dictionary key for target variable.
        :type target_key: str
        :return: The descriptive statistics as a dictionary.
        :rtype: list[dict[str, any]]
        """
        raise NotImplemented

    @abstractmethod
    async def count_where(self, data: list[dict[str, any]], group_by_key: list[str], target_key: str,
                          compare_value: float,
                          condition_type: Literal[">", ">=", "<", "<=", "==", "!="]) -> list[dict[str, any]]:
        """
        Check data with custom condition and returns the number of matches.
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: The dictionary key for data device.
        :type group_by_key: list[str]
        :param target_key: The dictionary key for value.
        :type target_key: str
        :param compare_value: The value to make the comparison
        :type compare_value: float
        :param condition_type: The type of condition to compare the data
        :type condition_type: Literal[">", ">=", "<", "<=", "==", "!="]
        """
        raise NotImplemented

    @abstractmethod
    async def sum_time_where(self, data: list[dict[str, any]], group_by_key: list[str], target_key: str,
                             timestamp_key: str, compare_value: float,
                             condition_type: Literal[">", ">=", "<", "<=", "==", "!="]) -> list[dict[str, any]]:
        """
        Check how much time n variables have maintained a conditional state and return the accumulated value.
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: The dictionary key for data device.
        :type group_by_key: list[str]
        :param target_key: The dictionary key for value.
        :type target_key: str
        :param timestamp_key: The dictionary key for timestamp.
        :type timestamp_key: str
        :param compare_value: The value to make the comparison
        :type compare_value: float
        :param condition_type: The type of condition to compare the data
        :type condition_type: Literal[">", ">=", "<", "<=", "==", "!="]
        """
        raise NotImplemented

    @abstractmethod
    async def sum_list_yaxis(self, data: list[dict[str, any]], group_by_key: list[str],
                              target_key: str) ->list[dict[str, any]]:
        """
        Converts a string representation of a list like '[1,4,532,23.2,3]' to float list and the sum all positions
        on axis=0.
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: Dictionary key to group data
        :type group_by_key: str
        :param target_key: Dictionary key where apply conversion
        :type target_key: str
        
        """
        raise NotImplemented

    @abstractmethod
    async def sum(self, data: List[Dict[str, any]], group_by_key: list[str], target_key: str) -> list[dict[str, any]]:
        """
        Sum data from specific key
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: Dictionary key to group data
        :type group_by_key: str
        :param target_key: Dictionary key where apply conversion
        :type target_key: str
        :return: The descriptive sum as list of dictionary.
        :rtype: list[dict[str, any]]
        """
        raise NotImplemented

    @abstractmethod
    async def get_max_row(self, data: list[dict[str, any]], group_by_key: list[str],
                          target_key: str) -> list[dict[str, any]]:
        """
        Get the max value in the different groups
        :param data: The input data as a list of dictionaries.
        :type data: List[Dict[str, any]]
        :param group_by_key: Dictionary key to group data
        :type group_by_key: str
        :param target_key: Dictionary key where apply conversion
        :type target_key: str
        :return: The descriptive sum as list of dictionary.
        :rtype: list[dict[str, any]]
        """
        raise NotImplemented

# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MapTheme(str, Enum):
    """
    MapTheme
    """

    """
    allowed enum values
    """
    LIGHT = 'light'
    DARK = 'dark'

    @classmethod
    def from_json(cls, json_str: str) -> MapTheme:
        """Create an instance of MapTheme from a JSON string"""
        return MapTheme(json.loads(json_str))


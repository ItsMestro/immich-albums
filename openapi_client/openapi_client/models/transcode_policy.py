# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TranscodePolicy(str, Enum):
    """
    TranscodePolicy
    """

    """
    allowed enum values
    """
    ALL = 'all'
    OPTIMAL = 'optimal'
    REQUIRED = 'required'
    DISABLED = 'disabled'

    @classmethod
    def from_json(cls, json_str: str) -> TranscodePolicy:
        """Create an instance of TranscodePolicy from a JSON string"""
        return TranscodePolicy(json.loads(json_str))



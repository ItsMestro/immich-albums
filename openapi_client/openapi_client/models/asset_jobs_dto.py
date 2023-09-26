# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.asset_job_name import AssetJobName

class AssetJobsDto(BaseModel):
    """
    AssetJobsDto
    """
    asset_ids: conlist(StrictStr) = Field(..., alias="assetIds")
    name: AssetJobName = Field(...)
    __properties = ["assetIds", "name"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AssetJobsDto:
        """Create an instance of AssetJobsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetJobsDto:
        """Create an instance of AssetJobsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetJobsDto.parse_obj(obj)

        _obj = AssetJobsDto.parse_obj({
            "asset_ids": obj.get("assetIds"),
            "name": obj.get("name")
        })
        return _obj



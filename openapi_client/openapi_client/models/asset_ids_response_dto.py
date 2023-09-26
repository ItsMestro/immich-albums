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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class AssetIdsResponseDto(BaseModel):
    """
    AssetIdsResponseDto
    """
    asset_id: StrictStr = Field(..., alias="assetId")
    error: Optional[StrictStr] = None
    success: StrictBool = Field(...)
    __properties = ["assetId", "error", "success"]

    @validator('error')
    def error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('duplicate', 'no_permission', 'not_found'):
            raise ValueError("must be one of enum values ('duplicate', 'no_permission', 'not_found')")
        return value

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
    def from_json(cls, json_str: str) -> AssetIdsResponseDto:
        """Create an instance of AssetIdsResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetIdsResponseDto:
        """Create an instance of AssetIdsResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetIdsResponseDto.parse_obj(obj)

        _obj = AssetIdsResponseDto.parse_obj({
            "asset_id": obj.get("assetId"),
            "error": obj.get("error"),
            "success": obj.get("success")
        })
        return _obj



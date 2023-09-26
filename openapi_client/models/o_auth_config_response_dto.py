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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class OAuthConfigResponseDto(BaseModel):
    """
    OAuthConfigResponseDto
    """
    auto_launch: Optional[StrictBool] = Field(None, alias="autoLaunch")
    button_text: Optional[StrictStr] = Field(None, alias="buttonText")
    enabled: StrictBool = Field(...)
    password_login_enabled: StrictBool = Field(..., alias="passwordLoginEnabled")
    url: Optional[StrictStr] = None
    __properties = ["autoLaunch", "buttonText", "enabled", "passwordLoginEnabled", "url"]

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
    def from_json(cls, json_str: str) -> OAuthConfigResponseDto:
        """Create an instance of OAuthConfigResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuthConfigResponseDto:
        """Create an instance of OAuthConfigResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthConfigResponseDto.parse_obj(obj)

        _obj = OAuthConfigResponseDto.parse_obj({
            "auto_launch": obj.get("autoLaunch"),
            "button_text": obj.get("buttonText"),
            "enabled": obj.get("enabled"),
            "password_login_enabled": obj.get("passwordLoginEnabled"),
            "url": obj.get("url")
        })
        return _obj



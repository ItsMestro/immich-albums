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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class PersonResponseDto(BaseModel):
    """
    PersonResponseDto
    """
    birth_date: Optional[date] = Field(..., alias="birthDate")
    id: StrictStr = Field(...)
    is_hidden: StrictBool = Field(..., alias="isHidden")
    name: StrictStr = Field(...)
    thumbnail_path: StrictStr = Field(..., alias="thumbnailPath")
    __properties = ["birthDate", "id", "isHidden", "name", "thumbnailPath"]

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
    def from_json(cls, json_str: str) -> PersonResponseDto:
        """Create an instance of PersonResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if birth_date (nullable) is None
        # and __fields_set__ contains the field
        if self.birth_date is None and "birth_date" in self.__fields_set__:
            _dict['birthDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonResponseDto:
        """Create an instance of PersonResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonResponseDto.parse_obj(obj)

        _obj = PersonResponseDto.parse_obj({
            "birth_date": obj.get("birthDate"),
            "id": obj.get("id"),
            "is_hidden": obj.get("isHidden"),
            "name": obj.get("name"),
            "thumbnail_path": obj.get("thumbnailPath")
        })
        return _obj



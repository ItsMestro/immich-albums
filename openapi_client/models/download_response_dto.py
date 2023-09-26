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
from pydantic import BaseModel, Field, StrictInt, conlist
from openapi_client.models.download_archive_info import DownloadArchiveInfo

class DownloadResponseDto(BaseModel):
    """
    DownloadResponseDto
    """
    archives: conlist(DownloadArchiveInfo) = Field(...)
    total_size: StrictInt = Field(..., alias="totalSize")
    __properties = ["archives", "totalSize"]

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
    def from_json(cls, json_str: str) -> DownloadResponseDto:
        """Create an instance of DownloadResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in archives (list)
        _items = []
        if self.archives:
            for _item in self.archives:
                if _item:
                    _items.append(_item.to_dict())
            _dict['archives'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DownloadResponseDto:
        """Create an instance of DownloadResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DownloadResponseDto.parse_obj(obj)

        _obj = DownloadResponseDto.parse_obj({
            "archives": [DownloadArchiveInfo.from_dict(_item) for _item in obj.get("archives")] if obj.get("archives") is not None else None,
            "total_size": obj.get("totalSize")
        })
        return _obj


# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel

class SeriesListLazyLoaded(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    value: Optional[List]
    is_loaded: Optional[bool]
    __properties = ["value", "isLoaded"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SeriesListLazyLoaded:
        """Create an instance of SeriesListLazyLoaded from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "value",
                            "is_loaded",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in value (list)
        _items = []
        if self.value:
            for _item in self.value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['value'] = _items
        # set to None if value (nullable) is None
        if self.value is None:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeriesListLazyLoaded:
        """Create an instance of SeriesListLazyLoaded from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SeriesListLazyLoaded.parse_obj(obj)

        _obj = SeriesListLazyLoaded.parse_obj({
            "value": [Series.from_dict(_item) for _item in obj.get("value")] if obj.get("value") is not None else None,
            "is_loaded": obj.get("isLoaded")
        })
        return _obj


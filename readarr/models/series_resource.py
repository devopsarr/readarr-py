# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from readarr.models.series_book_link_resource import SeriesBookLinkResource

class SeriesResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    links: Optional[List]
    __properties = ["id", "title", "description", "links"]

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
    def from_json(cls, json_str: str) -> SeriesResource:
        """Create an instance of SeriesResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if description (nullable) is None
        if self.description is None:
            _dict['description'] = None

        # set to None if links (nullable) is None
        if self.links is None:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeriesResource:
        """Create an instance of SeriesResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SeriesResource.parse_obj(obj)

        _obj = SeriesResource.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "links": [SeriesBookLinkResource.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj


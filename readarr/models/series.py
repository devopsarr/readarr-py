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


from typing import Optional
from pydantic import BaseModel

class Series(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    foreign_series_id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    numbered: Optional[bool]
    work_count: Optional[int]
    primary_work_count: Optional[int]
    link_items: Optional[SeriesBookLinkListLazyLoaded]
    books: Optional[BookListLazyLoaded]
    foreign_author_id: Optional[str]
    __properties = ["id", "foreignSeriesId", "title", "description", "numbered", "workCount", "primaryWorkCount", "linkItems", "books", "foreignAuthorId"]

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
    def from_json(cls, json_str: str) -> Series:
        """Create an instance of Series from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of link_items
        if self.link_items:
            _dict['linkItems'] = self.link_items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of books
        if self.books:
            _dict['books'] = self.books.to_dict()
        # set to None if foreign_series_id (nullable) is None
        if self.foreign_series_id is None:
            _dict['foreignSeriesId'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if description (nullable) is None
        if self.description is None:
            _dict['description'] = None

        # set to None if foreign_author_id (nullable) is None
        if self.foreign_author_id is None:
            _dict['foreignAuthorId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Series:
        """Create an instance of Series from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Series.parse_obj(obj)

        _obj = Series.parse_obj({
            "id": obj.get("id"),
            "foreign_series_id": obj.get("foreignSeriesId"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "numbered": obj.get("numbered"),
            "work_count": obj.get("workCount"),
            "primary_work_count": obj.get("primaryWorkCount"),
            "link_items": SeriesBookLinkListLazyLoaded.from_dict(obj.get("linkItems")) if obj.get("linkItems") is not None else None,
            "books": BookListLazyLoaded.from_dict(obj.get("books")) if obj.get("books") is not None else None,
            "foreign_author_id": obj.get("foreignAuthorId")
        })
        return _obj


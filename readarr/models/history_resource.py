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

from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel
from readarr.models.author_resource import AuthorResource
from readarr.models.book_resource import BookResource
from readarr.models.history_event_type import HistoryEventType
from readarr.models.quality_model import QualityModel

class HistoryResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    book_id: Optional[int]
    author_id: Optional[int]
    source_title: Optional[str]
    quality: Optional[QualityModel]
    quality_cutoff_not_met: Optional[bool]
    var_date: Optional[datetime]
    download_id: Optional[str]
    event_type: Optional[HistoryEventType]
    data: Optional[Dict]
    book: Optional[BookResource]
    author: Optional[AuthorResource]
    __properties = ["id", "bookId", "authorId", "sourceTitle", "quality", "qualityCutoffNotMet", "date", "downloadId", "eventType", "data", "book", "author"]

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
    def from_json(cls, json_str: str) -> HistoryResource:
        """Create an instance of HistoryResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of book
        if self.book:
            _dict['book'] = self.book.to_dict()
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # set to None if source_title (nullable) is None
        if self.source_title is None:
            _dict['sourceTitle'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if data (nullable) is None
        if self.data is None:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HistoryResource:
        """Create an instance of HistoryResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HistoryResource.parse_obj(obj)

        _obj = HistoryResource.parse_obj({
            "id": obj.get("id"),
            "book_id": obj.get("bookId"),
            "author_id": obj.get("authorId"),
            "source_title": obj.get("sourceTitle"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "quality_cutoff_not_met": obj.get("qualityCutoffNotMet"),
            "var_date": obj.get("date"),
            "download_id": obj.get("downloadId"),
            "event_type": obj.get("eventType"),
            "data": obj.get("data"),
            "book": BookResource.from_dict(obj.get("book")) if obj.get("book") is not None else None,
            "author": AuthorResource.from_dict(obj.get("author")) if obj.get("author") is not None else None
        })
        return _obj


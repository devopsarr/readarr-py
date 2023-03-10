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
from typing import List, Optional
from pydantic import BaseModel
from readarr.models.author_resource import AuthorResource
from readarr.models.download_protocol import DownloadProtocol
from readarr.models.quality_model import QualityModel

class BlacklistResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    author_id: Optional[int]
    book_ids: Optional[List]
    source_title: Optional[str]
    quality: Optional[QualityModel]
    var_date: Optional[datetime]
    protocol: Optional[DownloadProtocol]
    indexer: Optional[str]
    message: Optional[str]
    author: Optional[AuthorResource]
    __properties = ["id", "authorId", "bookIds", "sourceTitle", "quality", "date", "protocol", "indexer", "message", "author"]

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
    def from_json(cls, json_str: str) -> BlacklistResource:
        """Create an instance of BlacklistResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # set to None if book_ids (nullable) is None
        if self.book_ids is None:
            _dict['bookIds'] = None

        # set to None if source_title (nullable) is None
        if self.source_title is None:
            _dict['sourceTitle'] = None

        # set to None if indexer (nullable) is None
        if self.indexer is None:
            _dict['indexer'] = None

        # set to None if message (nullable) is None
        if self.message is None:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlacklistResource:
        """Create an instance of BlacklistResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return BlacklistResource.parse_obj(obj)

        _obj = BlacklistResource.parse_obj({
            "id": obj.get("id"),
            "author_id": obj.get("authorId"),
            "book_ids": obj.get("bookIds"),
            "source_title": obj.get("sourceTitle"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "var_date": obj.get("date"),
            "protocol": obj.get("protocol"),
            "indexer": obj.get("indexer"),
            "message": obj.get("message"),
            "author": AuthorResource.from_dict(obj.get("author")) if obj.get("author") is not None else None
        })
        return _obj


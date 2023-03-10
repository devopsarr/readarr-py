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
from readarr.models.author_title_info import AuthorTitleInfo
from readarr.models.quality_model import QualityModel

class ParsedBookInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    book_title: Optional[str]
    author_name: Optional[str]
    author_title_info: Optional[AuthorTitleInfo]
    quality: Optional[QualityModel]
    release_date: Optional[str]
    discography: Optional[bool]
    discography_start: Optional[int]
    discography_end: Optional[int]
    release_group: Optional[str]
    release_hash: Optional[str]
    release_version: Optional[str]
    __properties = ["bookTitle", "authorName", "authorTitleInfo", "quality", "releaseDate", "discography", "discographyStart", "discographyEnd", "releaseGroup", "releaseHash", "releaseVersion"]

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
    def from_json(cls, json_str: str) -> ParsedBookInfo:
        """Create an instance of ParsedBookInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author_title_info
        if self.author_title_info:
            _dict['authorTitleInfo'] = self.author_title_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if book_title (nullable) is None
        if self.book_title is None:
            _dict['bookTitle'] = None

        # set to None if author_name (nullable) is None
        if self.author_name is None:
            _dict['authorName'] = None

        # set to None if release_date (nullable) is None
        if self.release_date is None:
            _dict['releaseDate'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        if self.release_hash is None:
            _dict['releaseHash'] = None

        # set to None if release_version (nullable) is None
        if self.release_version is None:
            _dict['releaseVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParsedBookInfo:
        """Create an instance of ParsedBookInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParsedBookInfo.parse_obj(obj)

        _obj = ParsedBookInfo.parse_obj({
            "book_title": obj.get("bookTitle"),
            "author_name": obj.get("authorName"),
            "author_title_info": AuthorTitleInfo.from_dict(obj.get("authorTitleInfo")) if obj.get("authorTitleInfo") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "release_date": obj.get("releaseDate"),
            "discography": obj.get("discography"),
            "discography_start": obj.get("discographyStart"),
            "discography_end": obj.get("discographyEnd"),
            "release_group": obj.get("releaseGroup"),
            "release_hash": obj.get("releaseHash"),
            "release_version": obj.get("releaseVersion")
        })
        return _obj


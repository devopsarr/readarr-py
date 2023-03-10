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
from readarr.models.author_resource import AuthorResource
from readarr.models.book_resource import BookResource
from readarr.models.parsed_track_info import ParsedTrackInfo
from readarr.models.quality_model import QualityModel
from readarr.models.rejection import Rejection

class ManualImportResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    name: Optional[str]
    size: Optional[int]
    author: Optional[AuthorResource]
    book: Optional[BookResource]
    foreign_edition_id: Optional[str]
    quality: Optional[QualityModel]
    quality_weight: Optional[int]
    download_id: Optional[str]
    rejections: Optional[List]
    audio_tags: Optional[ParsedTrackInfo]
    additional_file: Optional[bool]
    replace_existing_files: Optional[bool]
    disable_release_switching: Optional[bool]
    __properties = ["id", "path", "name", "size", "author", "book", "foreignEditionId", "quality", "qualityWeight", "downloadId", "rejections", "audioTags", "additionalFile", "replaceExistingFiles", "disableReleaseSwitching"]

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
    def from_json(cls, json_str: str) -> ManualImportResource:
        """Create an instance of ManualImportResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of book
        if self.book:
            _dict['book'] = self.book.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item in self.rejections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rejections'] = _items
        # override the default output from pydantic by calling `to_dict()` of audio_tags
        if self.audio_tags:
            _dict['audioTags'] = self.audio_tags.to_dict()
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if foreign_edition_id (nullable) is None
        if self.foreign_edition_id is None:
            _dict['foreignEditionId'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualImportResource:
        """Create an instance of ManualImportResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ManualImportResource.parse_obj(obj)

        _obj = ManualImportResource.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "author": AuthorResource.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "book": BookResource.from_dict(obj.get("book")) if obj.get("book") is not None else None,
            "foreign_edition_id": obj.get("foreignEditionId"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "quality_weight": obj.get("qualityWeight"),
            "download_id": obj.get("downloadId"),
            "rejections": [Rejection.from_dict(_item) for _item in obj.get("rejections")] if obj.get("rejections") is not None else None,
            "audio_tags": ParsedTrackInfo.from_dict(obj.get("audioTags")) if obj.get("audioTags") is not None else None,
            "additional_file": obj.get("additionalFile"),
            "replace_existing_files": obj.get("replaceExistingFiles"),
            "disable_release_switching": obj.get("disableReleaseSwitching")
        })
        return _obj


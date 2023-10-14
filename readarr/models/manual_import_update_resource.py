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
from readarr.models.quality_model import QualityModel
from readarr.models.rejection import Rejection

class ManualImportUpdateResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    name: Optional[str]
    author_id: Optional[int]
    book_id: Optional[int]
    foreign_edition_id: Optional[str]
    quality: Optional[QualityModel]
    release_group: Optional[str]
    download_id: Optional[str]
    additional_file: Optional[bool]
    replace_existing_files: Optional[bool]
    disable_release_switching: Optional[bool]
    rejections: Optional[List]
    __properties = ["id", "path", "name", "authorId", "bookId", "foreignEditionId", "quality", "releaseGroup", "downloadId", "additionalFile", "replaceExistingFiles", "disableReleaseSwitching", "rejections"]

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
    def from_json(cls, json_str: str) -> ManualImportUpdateResource:
        """Create an instance of ManualImportUpdateResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item in self.rejections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rejections'] = _items
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if author_id (nullable) is None
        if self.author_id is None:
            _dict['authorId'] = None

        # set to None if book_id (nullable) is None
        if self.book_id is None:
            _dict['bookId'] = None

        # set to None if foreign_edition_id (nullable) is None
        if self.foreign_edition_id is None:
            _dict['foreignEditionId'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualImportUpdateResource:
        """Create an instance of ManualImportUpdateResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ManualImportUpdateResource.parse_obj(obj)

        _obj = ManualImportUpdateResource.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "name": obj.get("name"),
            "author_id": obj.get("authorId"),
            "book_id": obj.get("bookId"),
            "foreign_edition_id": obj.get("foreignEditionId"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "release_group": obj.get("releaseGroup"),
            "download_id": obj.get("downloadId"),
            "additional_file": obj.get("additionalFile"),
            "replace_existing_files": obj.get("replaceExistingFiles"),
            "disable_release_switching": obj.get("disableReleaseSwitching"),
            "rejections": [Rejection.from_dict(_item) for _item in obj.get("rejections")] if obj.get("rejections") is not None else None
        })
        return _obj


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

class RenameBookResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    author_id: Optional[int]
    book_id: Optional[int]
    book_file_id: Optional[int]
    existing_path: Optional[str]
    new_path: Optional[str]
    __properties = ["id", "authorId", "bookId", "bookFileId", "existingPath", "newPath"]

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
    def from_json(cls, json_str: str) -> RenameBookResource:
        """Create an instance of RenameBookResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if existing_path (nullable) is None
        if self.existing_path is None:
            _dict['existingPath'] = None

        # set to None if new_path (nullable) is None
        if self.new_path is None:
            _dict['newPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RenameBookResource:
        """Create an instance of RenameBookResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RenameBookResource.parse_obj(obj)

        _obj = RenameBookResource.parse_obj({
            "id": obj.get("id"),
            "author_id": obj.get("authorId"),
            "book_id": obj.get("bookId"),
            "book_file_id": obj.get("bookFileId"),
            "existing_path": obj.get("existingPath"),
            "new_path": obj.get("newPath")
        })
        return _obj


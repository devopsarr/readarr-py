# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.3.18.2411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class RenameBookResource(BaseModel):
    """
    RenameBookResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    author_id: Optional[StrictInt] = Field(default=None, alias="authorId")
    book_id: Optional[StrictInt] = Field(default=None, alias="bookId")
    book_file_id: Optional[StrictInt] = Field(default=None, alias="bookFileId")
    existing_path: Optional[StrictStr] = Field(default=None, alias="existingPath")
    new_path: Optional[StrictStr] = Field(default=None, alias="newPath")
    __properties: ClassVar[List[str]] = ["id", "authorId", "bookId", "bookFileId", "existingPath", "newPath"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RenameBookResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if existing_path (nullable) is None
        # and model_fields_set contains the field
        if self.existing_path is None and "existing_path" in self.model_fields_set:
            _dict['existingPath'] = None

        # set to None if new_path (nullable) is None
        # and model_fields_set contains the field
        if self.new_path is None and "new_path" in self.model_fields_set:
            _dict['newPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RenameBookResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "authorId": obj.get("authorId"),
            "bookId": obj.get("bookId"),
            "bookFileId": obj.get("bookFileId"),
            "existingPath": obj.get("existingPath"),
            "newPath": obj.get("newPath")
        })
        return _obj



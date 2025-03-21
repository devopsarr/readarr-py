# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.4.10.2734
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from readarr.models.tag_difference import TagDifference
from typing import Optional, Set
from typing_extensions import Self

class RetagBookResource(BaseModel):
    """
    RetagBookResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    author_id: Optional[StrictInt] = Field(default=None, alias="authorId")
    book_id: Optional[StrictInt] = Field(default=None, alias="bookId")
    track_numbers: Optional[List[StrictInt]] = Field(default=None, alias="trackNumbers")
    book_file_id: Optional[StrictInt] = Field(default=None, alias="bookFileId")
    path: Optional[StrictStr] = None
    changes: Optional[List[TagDifference]] = None
    __properties: ClassVar[List[str]] = ["id", "authorId", "bookId", "trackNumbers", "bookFileId", "path", "changes"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RetagBookResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item_changes in self.changes:
                if _item_changes:
                    _items.append(_item_changes.to_dict())
            _dict['changes'] = _items
        # set to None if track_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.track_numbers is None and "track_numbers" in self.model_fields_set:
            _dict['trackNumbers'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if changes (nullable) is None
        # and model_fields_set contains the field
        if self.changes is None and "changes" in self.model_fields_set:
            _dict['changes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetagBookResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "authorId": obj.get("authorId"),
            "bookId": obj.get("bookId"),
            "trackNumbers": obj.get("trackNumbers"),
            "bookFileId": obj.get("bookFileId"),
            "path": obj.get("path"),
            "changes": [TagDifference.from_dict(_item) for _item in obj["changes"]] if obj.get("changes") is not None else None
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class SeriesBookLink(BaseModel):
    """
    SeriesBookLink
    """ # noqa: E501
    id: Optional[StrictInt] = None
    position: Optional[StrictStr] = None
    series_position: Optional[StrictInt] = Field(default=None, alias="seriesPosition")
    series_id: Optional[StrictInt] = Field(default=None, alias="seriesId")
    book_id: Optional[StrictInt] = Field(default=None, alias="bookId")
    is_primary: Optional[StrictBool] = Field(default=None, alias="isPrimary")
    series: Optional[SeriesLazyLoaded] = None
    book: Optional[BookLazyLoaded] = None
    __properties: ClassVar[List[str]] = ["id", "position", "seriesPosition", "seriesId", "bookId", "isPrimary", "series", "book"]

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
        """Create an instance of SeriesBookLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of series
        if self.series:
            _dict['series'] = self.series.to_dict()
        # override the default output from pydantic by calling `to_dict()` of book
        if self.book:
            _dict['book'] = self.book.to_dict()
        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeriesBookLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "position": obj.get("position"),
            "seriesPosition": obj.get("seriesPosition"),
            "seriesId": obj.get("seriesId"),
            "bookId": obj.get("bookId"),
            "isPrimary": obj.get("isPrimary"),
            "series": SeriesLazyLoaded.from_dict(obj["series"]) if obj.get("series") is not None else None,
            "book": BookLazyLoaded.from_dict(obj["book"]) if obj.get("book") is not None else None
        })
        return _obj

from readarr.models.book_lazy_loaded import BookLazyLoaded
from readarr.models.series_lazy_loaded import SeriesLazyLoaded
# TODO: Rewrite to not use raise_errors
SeriesBookLink.model_rebuild(raise_errors=False)

